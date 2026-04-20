#!/usr/bin/env python3
"""
Kinsoul theme files upsert via Admin API (bypass Shopify CLI + theme-kit-access).

Uploads local files directly to a target theme via themeFilesUpsert mutation.
Useful when the CLI's theme-kit-access.shopifyapps.com endpoint is flaky.

Usage:
  python3 scripts/kinsoul-theme-files-upsert.py --theme=147526385750 \
    --file=sections/kinsoul-materials-sourcing.liquid \
    --file=sections/kinsoul-materials-durability.liquid \
    --file=templates/page.materials.json

Order matters: sections/*.liquid get uploaded before templates/*.json
(Shopify validates template references to sections at upload time).
"""
import sys
import json
import datetime
import argparse
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "scripts" / "shopify-admin-ops.log"
API_VERSION = "2026-04"
EXPECTED_STORE = "qr4xym-qi.myshopify.com"


def load_env():
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip().strip("'").strip('"')
    return env


def log_op(detail):
    ts = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    with LOG_PATH.open("a") as f:
        f.write(f"{ts} | themeFilesUpsert           | {detail}\n")


def gql(store, token, query, variables):
    endpoint = f"https://{store}/admin/api/{API_VERSION}/graphql.json"
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=payload,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Access-Token": token,
                 "Accept": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code}: {body[:600]}")
        sys.exit(2)


Q_UPSERT = """
mutation($themeId: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
  themeFilesUpsert(themeId: $themeId, files: $files) {
    upsertedThemeFiles { filename }
    userErrors { code filename message }
  }
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--theme", required=True, help="theme id (numeric)")
    ap.add_argument("--file", action="append", required=True, help="repo-relative path (can repeat)")
    ap.add_argument("--dry-run", action="store_true", help="preview upload order and file sizes, do not apply")
    args = ap.parse_args()

    env = load_env()
    if env.get("SHOPIFY_STORE") != EXPECTED_STORE:
        print(f"Refusing: unexpected store")
        sys.exit(1)
    token = env.get("SHOPIFY_ADMIN_API_TOKEN", "")
    if not token.startswith("shpat_"):
        print("Refusing: token prefix wrong")
        sys.exit(1)
    store = env["SHOPIFY_STORE"]

    # Order: sections → snippets → templates (template validates section refs)
    def sort_key(p):
        if p.startswith("sections/"):   return 0
        if p.startswith("snippets/"):   return 1
        if p.startswith("blocks/"):     return 2
        if p.startswith("assets/"):     return 3
        if p.startswith("config/"):     return 4
        if p.startswith("layout/"):     return 5
        if p.startswith("templates/"):  return 6
        if p.startswith("locales/"):    return 7
        return 99
    args.file.sort(key=sort_key)

    theme_gid = f"gid://shopify/OnlineStoreTheme/{args.theme}"

    # Confirm theme exists + role
    check = gql(store, token, """
      query($id: ID!) { theme(id: $id) { id name role } }
    """, {"id": theme_gid})
    if check.get("errors") or not check["data"].get("theme"):
        print(f"Theme {args.theme} not found or inaccessible.")
        sys.exit(2)
    t = check["data"]["theme"]
    print(f"Target theme: {t['name']!r} role={t['role']} id={t['id']}")
    if t["role"] == "MAIN":
        print("REFUSING: target is MAIN (live). This script is for unpublished themes only.")
        sys.exit(1)
    print(f"Upload order ({len(args.file)} file(s)):")
    for f in args.file:
        p = ROOT / f
        size = p.stat().st_size if p.exists() else 0
        exists = "ok" if p.exists() else "MISSING"
        print(f"  - {f}  ({size} bytes, {exists})")

    if args.dry_run:
        print("\nDRY RUN — no upload performed.")
        return

    # Upload in batches of 1 to guarantee strict ordering
    for filepath in args.file:
        p = ROOT / filepath
        if not p.exists():
            print(f"{filepath}: NOT FOUND locally")
            sys.exit(1)
        content = p.read_text()
        print(f"\n→ {filepath} ({len(content)} chars)")
        res = gql(store, token, Q_UPSERT, {
            "themeId": theme_gid,
            "files": [{"filename": filepath,
                       "body": {"type": "TEXT", "value": content}}],
        })
        if "errors" in res:
            print(f"  GraphQL errors: {res['errors']}")
            sys.exit(2)
        out = res["data"]["themeFilesUpsert"]
        ue = out.get("userErrors") or []
        if ue:
            print(f"  userErrors: {ue}")
            log_op(f"theme={args.theme} file={filepath} status=FAILED errors={ue}")
            sys.exit(2)
        upserted = [f["filename"] for f in out.get("upsertedThemeFiles", [])]
        print(f"  OK — upserted: {upserted}")
        log_op(f"theme={args.theme} file={filepath} status=OK")


if __name__ == "__main__":
    main()
