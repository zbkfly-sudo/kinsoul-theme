#!/usr/bin/env python3
"""
Kinsoul Blog Admin Setup — Journal launch automation.

Runs against the Shopify GraphQL Admin API (2026-04 — latest stable) to:
  1. Create the Journal blog (handle=journal, commentPolicy=CLOSED)
  2. Define 6 article-level metafield definitions
  3. Create /pages/our-studio (template=page.our-studio)

Reads from .env:
  SHOPIFY_STORE             — e.g. qr4xym-qi.myshopify.com
  SHOPIFY_ADMIN_API_TOKEN   — Admin API token from Custom App
                              Required scopes: write_content

Idempotent — re-running skips entities that already exist.

Usage:
  python3 scripts/kinsoul-blog-admin-setup.py [--dry-run]

Rollback (if needed):
  blogDelete / pageDelete / metafieldDefinitionDelete  (documented in
  SHOPIFY-ADMIN-API-POLICY.md §受控灰名单).
"""

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "scripts" / "shopify-admin-ops.log"
API_VERSION = "2026-04"
EXPECTED_STORE = "qr4xym-qi.myshopify.com"


def log_op(op, detail):
    import datetime
    ts = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    with LOG_PATH.open("a") as f:
        f.write(f"{ts} | {op:<26} | {detail}\n")


def load_env():
    env = {}
    if not ENV_PATH.exists():
        print(f"❌ .env not found at {ENV_PATH}")
        sys.exit(1)
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip("'").strip('"')
    return env


class ShopifyAdmin:
    def __init__(self, store, token):
        self.endpoint = f"https://{store}/admin/api/{API_VERSION}/graphql.json"
        self.token = token

    def query(self, query, variables=None):
        payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
        req = urllib.request.Request(
            self.endpoint,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": self.token,
                "Accept": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            print(f"❌ HTTP {e.code}: {body}")
            sys.exit(2)
        if "errors" in data:
            print(f"❌ GraphQL errors: {json.dumps(data['errors'], indent=2)}")
            sys.exit(2)
        return data["data"]


# ---------- Step 1 · Create Journal blog ----------

FIND_BLOG_QUERY = """
query findBlog($query: String!) {
  blogs(first: 5, query: $query) {
    edges { node { id handle title commentPolicy templateSuffix } }
  }
}
"""

CREATE_BLOG_MUTATION = """
mutation createBlog($blog: BlogCreateInput!) {
  blogCreate(blog: $blog) {
    blog { id handle title commentPolicy templateSuffix }
    userErrors { code field message }
  }
}
"""

JOURNAL_BLOG = {
    "title": "Journal",
    "handle": "journal",
    "commentPolicy": "CLOSED",
}


def create_journal_blog(client, dry_run):
    print("\n─── Step 1 · Journal blog ────────────────────────────────")
    existing = client.query(FIND_BLOG_QUERY, {"query": "handle:journal"})
    edges = existing["blogs"]["edges"]
    for edge in edges:
        if edge["node"]["handle"] == JOURNAL_BLOG["handle"]:
            print(f"  · Journal blog already exists (ID: {edge['node']['id']}) — skipping")
            return edge["node"]["id"]

    if dry_run:
        print(f"  · would create Journal blog (handle=journal, commentPolicy=CLOSED)")
        return None

    result = client.query(CREATE_BLOG_MUTATION, {"blog": JOURNAL_BLOG})
    errs = result["blogCreate"]["userErrors"]
    if errs:
        print(f"  ✗ failed: {errs}")
        log_op("blogCreate", f"handle=journal | status=FAILED | errors={errs}")
        return None
    blog = result["blogCreate"]["blog"]
    print(f"  ✓ created Journal blog (ID: {blog['id']})")
    log_op("blogCreate", f"handle=journal | id={blog['id']} | commentPolicy=CLOSED")
    return blog["id"]


# ---------- Step 2 · Article-level metafield definitions ----------

ARTICLE_METAFIELD_DEFS = [
    {
        "name": "Reading time (minutes)",
        "namespace": "custom",
        "key": "reading_time",
        "type": "number_integer",
        "ownerType": "ARTICLE",
        "description": "Estimated reading time in minutes, shown in article meta line.",
    },
    {
        "name": "Article category",
        "namespace": "custom",
        "key": "article_category",
        "type": "single_line_text_field",
        "ownerType": "ARTICLE",
        "description": "One of: materials / craft / gifting / care.",
    },
    {
        "name": "FAQ items (JSON)",
        "namespace": "custom",
        "key": "faq_items",
        "type": "json",
        "ownerType": "ARTICLE",
        "description": "Array of {question, answer} pairs rendered as FAQPage schema + accordion.",
    },
    {
        "name": "External sources",
        "namespace": "custom",
        "key": "external_sources",
        "type": "list.url",
        "ownerType": "ARTICLE",
        "description": "Tier-1 authoritative source URLs cited in this article (GIA/AGS/FTC/etc).",
    },
    {
        "name": "Kinsoul data present",
        "namespace": "custom",
        "key": "kinsoul_data_present",
        "type": "boolean",
        "ownerType": "ARTICLE",
        "description": "Self-check flag: true when the article contains ≥1 Kinsoul studio-specific fact. Hermes hard gate.",
    },
    {
        "name": "OG image override",
        "namespace": "custom",
        "key": "og_image_override",
        "type": "file_reference",
        "ownerType": "ARTICLE",
        "description": "Optional override for the social/OG preview image. Falls back to featured image.",
    },
    {
        "name": "Related products (blog)",
        "namespace": "custom",
        "key": "related_products",
        "type": "list.product_reference",
        "ownerType": "ARTICLE",
        "description": "Products mentioned / featured in the article, shown at article bottom.",
    },
]

METAFIELD_DEF_CREATE = """
mutation createDef($definition: MetafieldDefinitionInput!) {
  metafieldDefinitionCreate(definition: $definition) {
    createdDefinition { id key namespace type { name } ownerType }
    userErrors { code field message }
  }
}
"""


def create_article_metafield_defs(client, dry_run):
    print("\n─── Step 2 · Article metafield definitions ───────────────")
    for d in ARTICLE_METAFIELD_DEFS:
        if dry_run:
            print(f"  · {d['namespace']}.{d['key']:<22} would be defined ({d['type']}, owner={d['ownerType']})")
            continue

        result = client.query(METAFIELD_DEF_CREATE, {"definition": d})
        errs = result["metafieldDefinitionCreate"]["userErrors"]
        if errs:
            taken = any(e.get("code") == "TAKEN" for e in errs)
            if taken:
                print(f"  · {d['namespace']}.{d['key']:<22} already defined — skipping")
                log_op("metafieldDefinitionCreate", f"{d['namespace']}.{d['key']} | owner=ARTICLE | status=ALREADY_EXISTS")
            else:
                print(f"  ✗ {d['namespace']}.{d['key']:<22} failed: {errs}")
                log_op("metafieldDefinitionCreate", f"{d['namespace']}.{d['key']} | status=FAILED | errors={errs}")
        else:
            created = result["metafieldDefinitionCreate"]["createdDefinition"]
            print(f"  ✓ {d['namespace']}.{d['key']:<22} created (ID: {created['id']})")
            log_op("metafieldDefinitionCreate", f"{d['namespace']}.{d['key']} | owner=ARTICLE | id={created['id']} | type={d['type']}")


# ---------- Step 3 · Create /pages/our-studio ----------

FIND_PAGE_QUERY = """
query findPage($query: String!) {
  pages(first: 1, query: $query) {
    edges { node { id handle title templateSuffix } }
  }
}
"""

CREATE_PAGE_MUTATION = """
mutation createPage($page: PageCreateInput!) {
  pageCreate(page: $page) {
    page { id handle title templateSuffix }
    userErrors { field message code }
  }
}
"""

OUR_STUDIO_PAGE = {
    "title": "Our Studio",
    "handle": "our-studio",
    "templateSuffix": "our-studio",
    "body": "<p>Meet the Kinsoul Studio team behind the Journal. Full editorial transparency — how we research, write, edit, and verify every article.</p>",
    "isPublished": True,
}


def create_our_studio_page(client, dry_run):
    print("\n─── Step 3 · /pages/our-studio ───────────────────────────")
    existing = client.query(FIND_PAGE_QUERY, {"query": "handle:our-studio"})
    edges = existing["pages"]["edges"]
    if edges and edges[0]["node"]["handle"] == OUR_STUDIO_PAGE["handle"]:
        print(f"  · /pages/our-studio already exists (ID: {edges[0]['node']['id']}) — skipping")
        return edges[0]["node"]["id"]

    if dry_run:
        print(f"  · would create /pages/our-studio (template=our-studio, published=true)")
        return None

    result = client.query(CREATE_PAGE_MUTATION, {"page": OUR_STUDIO_PAGE})
    errs = result["pageCreate"]["userErrors"]
    if errs:
        print(f"  ✗ failed: {errs}")
        log_op("pageCreate", f"handle=our-studio | status=FAILED | errors={errs}")
        return None
    page = result["pageCreate"]["page"]
    print(f"  ✓ created /pages/our-studio (ID: {page['id']})")
    log_op("pageCreate", f"handle=our-studio | id={page['id']} | template={page['templateSuffix']}")
    return page["id"]


# ---------- Main ----------

def main():
    dry_run = "--dry-run" in sys.argv

    env = load_env()
    store = env.get("SHOPIFY_STORE")
    token = env.get("SHOPIFY_ADMIN_API_TOKEN")

    if not store:
        print("❌ SHOPIFY_STORE missing from .env")
        sys.exit(1)
    if store != EXPECTED_STORE:
        print(f"❌ SHOPIFY_STORE={store} does not match expected {EXPECTED_STORE}")
        sys.exit(1)
    if not token:
        print("❌ SHOPIFY_ADMIN_API_TOKEN missing from .env")
        sys.exit(1)
    if token.startswith("shpss_"):
        print("❌ SHOPIFY_ADMIN_API_TOKEN starts with 'shpss_' — that's the Client Secret, not an access token.")
        print("   Run scripts/shopify-exchange-token.py to get the correct access token.")
        sys.exit(1)

    print(f"Store: {store}")
    print(f"API:   {API_VERSION}")
    if dry_run:
        print("MODE:  dry-run (no writes)")
    else:
        print("MODE:  LIVE (will write to Shopify)")

    client = ShopifyAdmin(store, token)

    create_journal_blog(client, dry_run)
    create_article_metafield_defs(client, dry_run)
    create_our_studio_page(client, dry_run)

    print("\n✅ Done.")
    if dry_run:
        print("\nThis was a dry-run. To actually apply changes, re-run without --dry-run:")
        print("  python3 scripts/kinsoul-blog-admin-setup.py")
    else:
        print("\nNext: push the test theme and verify:")
        print(f"  https://{store}/admin/blogs")
        print(f"  → Journal blog should exist")
        print(f"  https://{store}/admin/pages")
        print(f"  → Our Studio page should exist and bind to page.our-studio template")
        print(f"  https://{store}/admin/settings/custom_data/article/metafields")
        print(f"  → 7 article metafields defined")


if __name__ == "__main__":
    main()
