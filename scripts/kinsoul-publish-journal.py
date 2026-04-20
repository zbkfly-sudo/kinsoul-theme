#!/usr/bin/env python3
"""
Kinsoul Journal Publisher — publish markdown drafts as Shopify articles.

Reads drafts/journal-2026-04-18/*.md (YAML frontmatter + markdown body),
converts body to HTML, and publishes to the Journal blog via
articleCreate + metafieldsSet (2026-04 Admin API).

First article publishes immediately; subsequent articles scheduled
at +2h and +4h (publishDate future ISO). Shopify automatically
makes each visible at its publishDate.

Usage:
  python3 scripts/kinsoul-publish-journal.py --dry-run
  python3 scripts/kinsoul-publish-journal.py --apply
  python3 scripts/kinsoul-publish-journal.py --apply --file 01-our-six-bracelets-material-breakdown.md
"""

import json
import re
import sys
import datetime
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "scripts" / "shopify-admin-ops.log"
DRAFTS_DIR = ROOT / "drafts" / "journal-2026-04-18"
API_VERSION = "2026-04"
EXPECTED_STORE = "qr4xym-qi.myshopify.com"
BLOG_HANDLE = "journal"

# Featured image per article (Shopify CDN URLs from existing product library)
FEATURED_IMAGES = {
    "our-six-bracelets-material-breakdown": {
        "url": "https://cdn.shopify.com/s/files/1/0714/7274/2486/files/8697aeb0aa7a4d4d174e88e88760ac56.jpg",
        "alt": "Six Kinsoul bracelets laid out — material-by-material breakdown",
    },
    "how-to-choose-your-kinsoul-bracelet": {
        "url": "https://cdn.shopify.com/s/files/1/0714/7274/2486/files/daf75a042a831fbed3574f67063b0875.jpg",
        "alt": "Serenity bracelet on neutral background — freeform amethyst with freshwater pearls",
    },
    "what-is-baroque-pearl": {
        "url": "https://cdn.shopify.com/s/files/1/0714/7274/2486/files/aura_logo.jpg",
        "alt": "Aura bracelet with central baroque pearl — natural irregular shape",
    },
}

# Publish schedule offsets from NOW (hours)
# Article 1 immediate, Article 2 +2h, Article 3 +4h
PUBLISH_OFFSETS_HOURS = {
    "our-six-bracelets-material-breakdown": 0,
    "how-to-choose-your-kinsoul-bracelet": 2,
    "what-is-baroque-pearl": 4,
}

AUTHOR_NAME = "Kevin"


def log_op(op, detail):
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with LOG_PATH.open("a") as f:
        f.write(f"{ts} | {op:<26} | {detail}\n")


def load_env():
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip("'").strip('"')
    return env


def parse_frontmatter(md_text):
    """Parse YAML-ish frontmatter from markdown. Returns (frontmatter_dict, body_markdown)."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", md_text, re.DOTALL)
    if not match:
        return {}, md_text
    fm_text, body = match.group(1), match.group(2)

    # Minimal YAML parser for our frontmatter (no external deps)
    fm = {}
    lines = fm_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val:
                # Scalar value (possibly quoted)
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                fm[key] = val
            else:
                # List or nested
                collected = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t")):
                    sub = lines[i].strip()
                    if sub.startswith("- question:"):
                        # FAQ item
                        q_text = sub[len("- question:"):].strip().strip('"')
                        # look for answer on next line
                        i += 1
                        if i < len(lines) and lines[i].strip().startswith("answer:"):
                            a_text = lines[i].strip()[len("answer:"):].strip().strip('"')
                            collected.append({"question": q_text, "answer": a_text})
                    elif sub.startswith("- "):
                        collected.append(sub[2:].strip())
                    i += 1
                fm[key] = collected
                continue
        i += 1
    return fm, body


def md_to_html(md):
    """Lightweight markdown → HTML. Handles H1/H2/H3, **bold**, *italic*,
    [text](url), -lists, |tables|, paragraphs, hr."""
    # Strip the first H1 if present (Shopify article uses title separately).
    # Use leading-whitespace-tolerant regex because body from parse_frontmatter
    # often starts with a \n.
    md = md.lstrip()
    md = re.sub(r"^# .+\n\n?", "", md, count=1)

    lines = md.split("\n")
    html_parts = []
    i = 0
    in_list = False
    in_table = False
    table_buf = []

    def close_list():
        nonlocal in_list
        if in_list:
            html_parts.append("</ul>")
            in_list = False

    def inline(s):
        # links
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        # bold
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        # italic (avoid collision with bold — only single asterisks with non-space around)
        s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
        return s

    def flush_table():
        nonlocal in_table, table_buf
        if not table_buf:
            return
        html_parts.append('<table>')
        for idx, row in enumerate(table_buf):
            # parse pipe row
            cells = [c.strip() for c in row.strip("|").split("|")]
            if idx == 0:
                html_parts.append("<thead><tr>")
                for c in cells:
                    html_parts.append(f"<th>{inline(c)}</th>")
                html_parts.append("</tr></thead><tbody>")
            elif re.match(r"^\s*[-:\s|]+\s*$", row):
                continue  # separator line
            else:
                html_parts.append("<tr>")
                for c in cells:
                    html_parts.append(f"<td>{inline(c)}</td>")
                html_parts.append("</tr>")
        html_parts.append("</tbody></table>")
        table_buf = []
        in_table = False

    while i < len(lines):
        line = lines[i]

        # Table start
        if line.startswith("|") and "|" in line[1:]:
            if not in_table:
                in_table = True
                close_list()
            table_buf.append(line)
            i += 1
            continue
        elif in_table:
            flush_table()

        # Blank line → paragraph break
        if line.strip() == "":
            close_list()
            i += 1
            continue

        # Horizontal rule
        if line.strip() == "---":
            close_list()
            html_parts.append("<hr>")
            i += 1
            continue

        # Headings
        if line.startswith("### "):
            close_list()
            html_parts.append(f"<h3>{inline(line[4:].strip())}</h3>")
            i += 1
            continue
        if line.startswith("## "):
            close_list()
            html_parts.append(f"<h2>{inline(line[3:].strip())}</h2>")
            i += 1
            continue
        if line.startswith("# "):
            close_list()
            html_parts.append(f"<h1>{inline(line[2:].strip())}</h1>")
            i += 1
            continue

        # List item
        if line.startswith("- "):
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append(f"<li>{inline(line[2:].strip())}</li>")
            i += 1
            continue

        # Default: paragraph (collect consecutive non-blank lines)
        close_list()
        para_lines = [line]
        j = i + 1
        while j < len(lines) and lines[j].strip() and not any(
            lines[j].startswith(prefix) for prefix in ("#", "- ", "|", "---")
        ):
            para_lines.append(lines[j])
            j += 1
        para = " ".join(l.strip() for l in para_lines)
        html_parts.append(f"<p>{inline(para)}</p>")
        i = j

    close_list()
    if in_table:
        flush_table()
    return "\n".join(html_parts)


class ShopifyAdmin:
    def __init__(self, store, token):
        self.endpoint = f"https://{store}/admin/api/{API_VERSION}/graphql.json"
        self.token = token

    def query(self, q, variables=None):
        payload = json.dumps({"query": q, "variables": variables or {}}).encode()
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
            print(f"❌ HTTP {e.code}: {body[:500]}")
            sys.exit(2)
        if "errors" in data:
            print(f"❌ GraphQL errors: {json.dumps(data['errors'], indent=2)}")
            sys.exit(2)
        return data["data"]


Q_FIND_BLOG = """
query($query: String!) {
  blogs(first: 5, query: $query) {
    edges { node { id handle title } }
  }
}
"""

Q_ARTICLE_CREATE = """
mutation createArticle($article: ArticleCreateInput!) {
  articleCreate(article: $article) {
    article {
      id
      title
      handle
      publishedAt
    }
    userErrors { code field message }
  }
}
"""

Q_ARTICLE_UPDATE = """
mutation updateArticle($id: ID!, $article: ArticleUpdateInput!) {
  articleUpdate(id: $id, article: $article) {
    article { id handle }
    userErrors { code field message }
  }
}
"""

Q_FIND_ARTICLE_BY_HANDLE = """
query($query: String!) {
  articles(first: 5, query: $query) {
    edges { node { id handle blog { handle } } }
  }
}
"""

Q_METAFIELDS_SET = """
mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { id key namespace }
    userErrors { field message }
  }
}
"""


def publish_article(client, md_path, blog_id, dry_run=False):
    print(f"\n─── {md_path.name} ───")
    text = md_path.read_text()
    fm, body_md = parse_frontmatter(text)

    slug = fm.get("slug")
    title = fm.get("title")
    if not slug or not title:
        print(f"  ✗ missing slug or title in frontmatter")
        return None

    # Compute publish time. Shopify 2026-04 rule:
    #   - isPublished=true + NO publishDate → publishes immediately
    #   - isPublished=false + future publishDate → scheduled (Shopify auto-publishes at that time)
    #   - isPublished=true + future publishDate → ERROR (can't combine)
    offset_hours = PUBLISH_OFFSETS_HOURS.get(slug, 0)
    publish_iso = None
    if offset_hours > 0:
        publish_at = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=offset_hours)
        publish_iso = publish_at.isoformat(timespec="seconds")

    body_html = md_to_html(body_md)
    img = FEATURED_IMAGES.get(slug)

    # tags: comma-separated string per Shopify API
    tags_list = fm.get("tags", [])
    tags_str = ", ".join(tags_list) if isinstance(tags_list, list) else str(tags_list)

    article_input = {
        "blogId": blog_id,
        "title": title,
        "handle": slug,
        "author": {"name": AUTHOR_NAME},
        "body": body_html,
        "summary": fm.get("meta_description", "")[:400],
        "tags": tags_list,
    }
    if publish_iso is None:
        # immediate publish
        article_input["isPublished"] = True
    else:
        # scheduled — must be unpublished + future publishDate
        article_input["isPublished"] = False
        article_input["publishDate"] = publish_iso
    if img:
        article_input["image"] = {"altText": img["alt"], "url": img["url"]}

    print(f"  · title: {title}")
    print(f"  · slug: {slug}")
    print(f"  · tags: {tags_str}")
    if publish_iso is None:
        print(f"  · publishAt: NOW (immediate)")
    else:
        print(f"  · publishAt: {publish_iso}  (scheduled +{offset_hours}h, isPublished=false)")
    print(f"  · body HTML length: {len(body_html)}")
    print(f"  · author: {AUTHOR_NAME}")
    print(f"  · featured image: {img['url'] if img else '(none)'}")

    if dry_run:
        print(f"  · [dry-run] would articleCreate + metafieldsSet")
        return None

    result = client.query(Q_ARTICLE_CREATE, {"article": article_input})
    errs = result["articleCreate"]["userErrors"]
    if errs:
        print(f"  ✗ articleCreate failed: {errs}")
        log_op("articleCreate", f"handle={slug} | status=FAILED | errors={errs}")
        return None

    article = result["articleCreate"]["article"]
    aid = article["id"]
    print(f"  ✓ articleCreate OK (ID: {aid})")
    log_op("articleCreate", f"handle={slug} | id={aid} | publishAt={publish_iso}")

    # Set metafields
    metafields = [
        {
            "ownerId": aid,
            "namespace": "custom",
            "key": "reading_time",
            "type": "number_integer",
            "value": str(fm.get("reading_time", 5)),
        },
        {
            "ownerId": aid,
            "namespace": "custom",
            "key": "article_category",
            "type": "single_line_text_field",
            "value": fm.get("category", "materials"),
        },
        {
            "ownerId": aid,
            "namespace": "custom",
            "key": "kinsoul_data_present",
            "type": "boolean",
            "value": "true",
        },
    ]
    # faq_items (JSON)
    faq = fm.get("faq_items", [])
    if faq:
        metafields.append({
            "ownerId": aid,
            "namespace": "custom",
            "key": "faq_items",
            "type": "json",
            "value": json.dumps(faq),
        })
    # external_sources (list.url)
    sources = fm.get("external_sources", [])
    if sources:
        metafields.append({
            "ownerId": aid,
            "namespace": "custom",
            "key": "external_sources",
            "type": "list.url",
            "value": json.dumps(sources),
        })

    mf_result = client.query(Q_METAFIELDS_SET, {"metafields": metafields})
    mf_errs = mf_result["metafieldsSet"]["userErrors"]
    if mf_errs:
        print(f"  ⚠️  metafieldsSet had errors: {mf_errs}")
        log_op("metafieldsSet", f"article={slug} | count={len(metafields)} | errors={mf_errs}")
    else:
        count = len(mf_result["metafieldsSet"]["metafields"])
        print(f"  ✓ metafieldsSet OK ({count} metafields)")
        log_op("metafieldsSet", f"article={slug} | count={count} | status=OK")

    return aid


def main():
    dry_run = "--dry-run" in sys.argv
    apply = "--apply" in sys.argv
    file_filter = None
    for i, a in enumerate(sys.argv):
        if a == "--file" and i + 1 < len(sys.argv):
            file_filter = sys.argv[i + 1]

    if not dry_run and not apply:
        print("Usage: python3 scripts/kinsoul-publish-journal.py [--dry-run | --apply] [--file <name>]")
        sys.exit(1)

    env = load_env()
    store = env.get("SHOPIFY_STORE")
    token = env.get("SHOPIFY_ADMIN_API_TOKEN")
    if store != EXPECTED_STORE:
        print(f"❌ unexpected store: {store}")
        sys.exit(1)
    if not token:
        print("❌ SHOPIFY_ADMIN_API_TOKEN missing")
        sys.exit(1)

    client = ShopifyAdmin(store, token)

    # Resolve Journal blog ID
    res = client.query(Q_FIND_BLOG, {"query": f"handle:{BLOG_HANDLE}"})
    edges = res["blogs"]["edges"]
    if not edges:
        print(f"❌ Journal blog (handle={BLOG_HANDLE}) not found")
        sys.exit(1)
    blog_id = edges[0]["node"]["id"]
    print(f"Blog:  {edges[0]['node']['title']} (id={blog_id})")
    print(f"Mode:  {'DRY-RUN' if dry_run else 'LIVE'}")

    # Collect draft files in publish order
    files = sorted(DRAFTS_DIR.glob("*.md"))
    if file_filter:
        files = [f for f in files if file_filter in f.name]
    if not files:
        print("❌ no markdown files found")
        sys.exit(1)

    for f in files:
        publish_article(client, f, blog_id, dry_run=dry_run)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
