#!/usr/bin/env python3
"""
Kinsoul Admin Setup — one-shot automation for the post-redesign Admin tasks.

Runs against the Shopify GraphQL Admin API (2026-01) to:
  1. Create 3 pages (Stone Quiz / Compare / Gifting Guide) with matching templates
  2. Define 2 product metafield definitions (custom.related_products + custom.stone_chip)
  3. Fill related_products + stone_chip values for all 6 bracelets
  4. Re-point the homepage hero secondary CTA to /pages/stone-quiz (via theme settings)

Reads from .env:
  SHOPIFY_STORE             — e.g. qr4xym-qi.myshopify.com
  SHOPIFY_ADMIN_API_TOKEN   — Admin API token from the Custom App (NEW, not the Theme token)

Idempotent — re-running skips entities that already exist.

Usage:
  python3 scripts/kinsoul-admin-setup.py [--dry-run]
"""

import os
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "scripts" / "shopify-admin-ops.log"
API_VERSION = "2026-01"
EXPECTED_STORE = "qr4xym-qi.myshopify.com"  # per SHOPIFY-ADMIN-API-POLICY.md

def log_op(op, detail):
    """Append one-line audit entry per SHOPIFY-ADMIN-API-POLICY.md §审计日志."""
    import datetime
    ts = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    with LOG_PATH.open("a") as f:
        f.write(f"{ts} | {op:<18} | {detail}\n")

# ---------- Load .env ----------
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

# ---------- GraphQL client ----------
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

# ---------- Step 1 — Create pages ----------
PAGES = [
    {
        "title": "Stone Quiz",
        "handle": "stone-quiz",
        "template_suffix": "quiz",
        "body": "<p>Not sure which Kinsoul bracelet is right for you? Answer three short questions and we'll match you to the piece that fits how you want to feel, what you'll spend, and when you'll wear it.</p>",
        "seo_title": "Find Your Stone — 3-Question Bracelet Quiz | Kinsoul Energy",
        "seo_desc": "Not sure which Kinsoul bracelet is right for you? Answer 3 short questions about feeling, budget, and occasion — we'll match you to the piece that fits.",
    },
    {
        "title": "Compare Bracelets",
        "handle": "compare",
        "template_suffix": "compare",
        "body": "<p>Side-by-side comparison of every Kinsoul bracelet: stone, pearl, metal, price, and best worn. Pick the one that fits your wrist and your day.</p>",
        "seo_title": "Compare All 6 Bracelets — Kinsoul Energy",
        "seo_desc": "Side-by-side comparison of every Kinsoul bracelet: stone, pearl, metal, price, and best worn. Pick the one that fits your wrist and your day.",
    },
    {
        "title": "Gifting Guide",
        "handle": "gifting-guide",
        "template_suffix": "gifting-guide",
        "body": "<p>Handmade gemstone + pearl bracelets for birthdays, anniversaries, holidays, and self-gifting. Each piece arrives gift-ready.</p>",
        "seo_title": "Gifting Guide — Kinsoul Bracelets by Occasion & Budget",
        "seo_desc": "Handmade gemstone + pearl bracelets for birthdays, anniversaries, holidays, and self-gifting. Each piece arrives gift-ready. Under $200 to $365.",
    },
]

FIND_PAGE_QUERY = """
query findPage($handle: String!) {
  pages(first: 1, query: $handle) {
    edges {
      node { id handle title templateSuffix }
    }
  }
}
"""

CREATE_PAGE_MUTATION = """
mutation createPage($page: PageCreateInput!) {
  pageCreate(page: $page) {
    page { id handle title templateSuffix }
    userErrors { field message }
  }
}
"""

def create_pages(client, dry_run):
    print("\n─── Step 1 · Pages ─────────────────────────────────────")
    for p in PAGES:
        existing = client.query(FIND_PAGE_QUERY, {"handle": f"handle:{p['handle']}"})
        edges = existing["pages"]["edges"]
        if edges and edges[0]["node"]["handle"] == p["handle"]:
            print(f"  · {p['title']:<20} already exists (ID: {edges[0]['node']['id']}) — skipping")
            continue

        if dry_run:
            print(f"  · {p['title']:<20} would be created (handle={p['handle']}, template={p['template_suffix']})")
            continue

        page_input = {
            "title": p["title"],
            "handle": p["handle"],
            "body": p["body"],
            "templateSuffix": p["template_suffix"],
            "isPublished": True,
        }
        result = client.query(CREATE_PAGE_MUTATION, {"page": page_input})
        errs = result["pageCreate"]["userErrors"]
        if errs:
            print(f"  ✗ {p['title']:<20} failed: {errs}")
            log_op("pageCreate", f"handle={p['handle']} | status=FAILED | errors={errs}")
        else:
            page = result["pageCreate"]["page"]
            print(f"  ✓ {p['title']:<20} created (ID: {page['id']}, template: {page['templateSuffix']})")
            log_op("pageCreate", f"handle={p['handle']} | id={page['id']} | template={page['templateSuffix']}")

# ---------- Step 2 — Metafield definitions ----------
METAFIELD_DEFS = [
    {
        "name": "Related products (Complete Your Look)",
        "namespace": "custom",
        "key": "related_products",
        "type": "list.product_reference",
        "ownerType": "PRODUCT",
        "description": "Manual related products shown in Complete Your Look on PDP.",
    },
    {
        "name": "Stone chip label",
        "namespace": "custom",
        "key": "stone_chip",
        "type": "single_line_text_field",
        "ownerType": "PRODUCT",
        "description": "Short stone name shown on product card chip (e.g. 'Red Agate').",
    },
]

METAFIELD_DEF_CREATE_MUTATION = """
mutation createDef($definition: MetafieldDefinitionInput!) {
  metafieldDefinitionCreate(definition: $definition) {
    createdDefinition { id key namespace type { name } }
    userErrors { field message code }
  }
}
"""

def create_metafield_definitions(client, dry_run):
    print("\n─── Step 2 · Metafield definitions ────────────────────")
    for d in METAFIELD_DEFS:
        if dry_run:
            print(f"  · {d['namespace']}.{d['key']:<20} would be defined (type: {d['type']})")
            continue
        result = client.query(METAFIELD_DEF_CREATE_MUTATION, {"definition": d})
        errs = result["metafieldDefinitionCreate"]["userErrors"]
        if errs:
            taken = any(e.get("code") == "TAKEN" for e in errs)
            if taken:
                print(f"  · {d['namespace']}.{d['key']:<20} already defined — skipping")
                log_op("metafieldDefinitionCreate", f"{d['namespace']}.{d['key']} | status=ALREADY_EXISTS")
            else:
                print(f"  ✗ {d['namespace']}.{d['key']:<20} failed: {errs}")
                log_op("metafieldDefinitionCreate", f"{d['namespace']}.{d['key']} | status=FAILED | errors={errs}")
        else:
            definition = result["metafieldDefinitionCreate"]["createdDefinition"]
            print(f"  ✓ {d['namespace']}.{d['key']:<20} created (ID: {definition['id']})")
            log_op("metafieldDefinitionCreate", f"{d['namespace']}.{d['key']} | id={definition['id']} | type={d['type']}")

# ---------- Step 3 — Fill metafield values ----------
# Product handles fixed at time of audit (per CLAUDE.md)
PRODUCT_MAP = {
    "ember":    "persian-red-agate-pearl-sterling-silver-bracelet",
    "serenity": "freeform-amethyst-bracelet-with-freshwater-pearls",
    "aura":     "aura-balance-bracelet-baroque-pearl-crystal-mixed-gemstones",
    "obsidian": "mozhu-persian-agate-baroque-pearl-bracelet",
    "terra":    "moqiao-black-agate-rutilated-quartz-pearl-bracelet",
    "soleil":   "zining-brazilian-yellow-quartz-clear-quartz-amethyst-bracelet",
}

STONE_CHIP = {
    "ember":    "Red Agate",
    "serenity": "Amethyst",
    "aura":     "Multi-stone",
    "obsidian": "Black Agate",
    "terra":    "Banded Agate",
    "soleil":   "Citrine",
}

# Pairing rules from ADMIN-TASKS-P2-RELATED.md
RELATED = {
    "ember":    ["obsidian", "terra", "aura"],
    "serenity": ["soleil", "ember", "aura"],
    "aura":     ["ember", "terra", "obsidian"],
    "obsidian": ["ember", "terra", "aura"],
    "terra":    ["ember", "obsidian", "aura"],
    "soleil":   ["serenity", "ember", "aura"],
}

PRODUCT_BY_HANDLE_QUERY = """
query productByHandle($handle: String!) {
  productByHandle(handle: $handle) {
    id
    handle
    title
  }
}
"""

METAFIELDS_SET_MUTATION = """
mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { id key namespace value type }
    userErrors { field message }
  }
}
"""

def resolve_product_ids(client):
    ids = {}
    for slug, handle in PRODUCT_MAP.items():
        result = client.query(PRODUCT_BY_HANDLE_QUERY, {"handle": handle})
        product = result.get("productByHandle")
        if not product:
            print(f"  ✗ {slug:<10} (handle={handle}) — PRODUCT NOT FOUND")
            continue
        ids[slug] = product["id"]
    return ids

def fill_metafield_values(client, dry_run):
    print("\n─── Step 3 · Fill product metafield values ────────────")
    print("  · Resolving 6 product IDs by handle...")
    ids = resolve_product_ids(client)
    missing = set(PRODUCT_MAP) - set(ids)
    if missing:
        print(f"  ⚠️  Missing products: {missing} — they won't get metafield values")

    metafields = []
    for slug, pid in ids.items():
        # stone_chip
        metafields.append({
            "ownerId": pid,
            "namespace": "custom",
            "key": "stone_chip",
            "type": "single_line_text_field",
            "value": STONE_CHIP[slug],
        })
        # related_products (JSON-stringified list of GIDs, in order)
        related_ids = [ids[rel] for rel in RELATED[slug] if rel in ids]
        metafields.append({
            "ownerId": pid,
            "namespace": "custom",
            "key": "related_products",
            "type": "list.product_reference",
            "value": json.dumps(related_ids),
        })

    if dry_run:
        for m in metafields:
            label = f"{m['namespace']}.{m['key']}"
            val = m['value'] if len(m['value']) < 60 else m['value'][:57] + "..."
            print(f"  · would set {label:<28} on {m['ownerId'][-12:]}: {val}")
        return

    # Batch in chunks of 25 (API limit)
    BATCH = 25
    for i in range(0, len(metafields), BATCH):
        chunk = metafields[i:i+BATCH]
        result = client.query(METAFIELDS_SET_MUTATION, {"metafields": chunk})
        errs = result["metafieldsSet"]["userErrors"]
        if errs:
            print(f"  ✗ batch {i//BATCH + 1} errors: {errs}")
            log_op("metafieldsSet", f"batch={i//BATCH + 1} | count={len(chunk)} | status=FAILED | errors={errs}")
        else:
            print(f"  ✓ batch {i//BATCH + 1}: set {len(chunk)} metafields")
            log_op("metafieldsSet", f"batch={i//BATCH + 1} | count={len(chunk)} | status=OK")

# ---------- Main ----------
def main():
    dry_run = "--dry-run" in sys.argv

    env = load_env()
    store = env.get("SHOPIFY_STORE")
    token = env.get("SHOPIFY_ADMIN_API_TOKEN")

    if not store:
        print("❌ SHOPIFY_STORE missing from .env")
        sys.exit(1)

    # Domain sanity — per SHOPIFY-ADMIN-API-POLICY.md §"立即停止的信号"
    if store != EXPECTED_STORE:
        print(f"❌ SHOPIFY_STORE={store} does not match expected {EXPECTED_STORE}")
        print("   Stopping — verify you're pointing at the right store.")
        sys.exit(1)
    # Token format sanity check — per SHOPIFY-ADMIN-API-POLICY.md §"立即停止的信号"
    if token and not token.startswith("shpat_"):
        print(f"""
❌ SHOPIFY_ADMIN_API_TOKEN has wrong prefix: '{token.split('_')[0]}_'

   Valid Admin API access token starts with 'shpat_'.
   You likely pasted the Client Secret (shpss_) or API key instead.

   In the Custom App's "API credentials" tab:
   - shpss_… = API secret key (Client Secret) — used for OAuth, NOT for this
   - shpat_… = Admin API access token — THIS IS WHAT WE NEED

   Look for the "Admin API access token" section specifically. If it says
   "You'll only see this token once" and the value is hidden, Uninstall the
   app and Install again — the token re-displays on fresh install.
""")
        sys.exit(1)

    if not token:
        print("""
❌ SHOPIFY_ADMIN_API_TOKEN missing from .env

   You need to create a Custom App in Shopify to get this token.

   1. Shopify Admin → Settings → Apps and sales channels
      → Develop apps → Build apps (opens Dev Dashboard)
   2. Create app → name it "Kinsoul Admin Ops"
   3. Configuration → Admin API access scopes, check:
      ✓ write_products
      ✓ write_content  (or write_online_store_pages)
      ✓ write_files
      ✓ read_products, read_content, read_files (usually auto)
   4. Install app on this store
   5. Copy the Admin API access token
   6. Add to .env as:
      SHOPIFY_ADMIN_API_TOKEN=shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxx

   Then run this script again.
""")
        sys.exit(1)

    print(f"Store: {store}")
    print(f"API:   {API_VERSION}")
    if dry_run:
        print("MODE:  dry-run (no writes)")
    else:
        print("MODE:  LIVE (will write to Shopify)")

    client = ShopifyAdmin(store, token)

    create_pages(client, dry_run)
    create_metafield_definitions(client, dry_run)
    fill_metafield_values(client, dry_run)

    print("\n✅ Done.")
    print("\nNext: preview your test theme and confirm:")
    print(f"  https://{store}/?preview_theme_id=147445907542")
    print("  → /pages/stone-quiz should render")
    print("  → /pages/compare should render")
    print("  → /pages/gifting-guide should render")
    print("  → any PDP's Complete Your Look should show 3 related products")
    print("  → every product card should have a stone chip")

if __name__ == "__main__":
    main()
