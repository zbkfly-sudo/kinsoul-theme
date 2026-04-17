#!/usr/bin/env python3
"""
Clean up accumulated test themes, keeping:
  - The current live theme (from .env SHOPIFY_LIVE_THEME_ID)
  - The single most recent test theme (for preview continuity)
  - Any theme passed via --keep <id>,<id>,...

Before deleting, prints a plan for user confirmation unless --yes is passed.

Uses Admin API 2026-01 themeDelete mutation (requires write_themes scope,
which our Custom App already has).
"""
import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
API_VERSION = "2026-01"

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

class ShopifyAdmin:
    def __init__(self, store, token):
        self.endpoint = f"https://{store}/admin/api/{API_VERSION}/graphql.json"
        self.token = token

    def query(self, query, variables=None):
        payload = json.dumps({"query": query, "variables": variables or {}}).encode()
        req = urllib.request.Request(
            self.endpoint,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": self.token,
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
        if "errors" in data:
            print(f"❌ GraphQL errors: {json.dumps(data['errors'], indent=2)}")
            sys.exit(2)
        return data["data"]

LIST_THEMES_QUERY = """
query {
  themes(first: 50) {
    edges {
      node {
        id
        name
        role
        createdAt
      }
    }
  }
}
"""

DELETE_THEME_MUTATION = """
mutation themeDelete($id: ID!) {
  themeDelete(id: $id) {
    deletedThemeId
    userErrors { field message }
  }
}
"""

def gid_to_int(gid):
    """gid://shopify/Theme/147445907542 → 147445907542"""
    return int(gid.rsplit("/", 1)[-1])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    ap.add_argument("--keep", default="", help="Extra theme IDs to keep, comma-separated")
    ap.add_argument("--keep-latest", type=int, default=1,
                    help="Keep N most recent test themes (default: 1)")
    args = ap.parse_args()

    env = load_env()
    store = env.get("SHOPIFY_STORE", "").strip()
    token = env.get("SHOPIFY_ADMIN_API_TOKEN", "").strip()
    live_id = env.get("SHOPIFY_LIVE_THEME_ID", "").strip()

    if not store or not token or not live_id:
        print("❌ .env missing SHOPIFY_STORE / SHOPIFY_ADMIN_API_TOKEN / SHOPIFY_LIVE_THEME_ID")
        sys.exit(1)

    client = ShopifyAdmin(store, token)
    data = client.query(LIST_THEMES_QUERY)
    themes = [e["node"] for e in data["themes"]["edges"]]
    themes.sort(key=lambda t: t["createdAt"], reverse=True)

    # Build keep set
    keep = {int(live_id)}
    for extra in args.keep.split(","):
        extra = extra.strip()
        if extra:
            keep.add(int(extra))

    # Auto-keep N most recent non-live test themes
    non_live = [t for t in themes if gid_to_int(t["id"]) != int(live_id)]
    for t in non_live[:args.keep_latest]:
        keep.add(gid_to_int(t["id"]))

    print(f"\nStore: {store}")
    print(f"Live theme: {live_id}")
    print(f"Total themes: {len(themes)}\n")

    to_delete = []
    print(f"{'Theme ID':<16}  {'Role':<11}  Name")
    print("-" * 70)
    for t in themes:
        tid = gid_to_int(t["id"])
        role = t["role"] or ""
        status = "KEEP" if tid in keep else "DELETE"
        marker = "🔒" if tid in keep else "🗑️ "
        print(f"{marker} {tid:<14}  {role:<11}  {t['name']}")
        if tid not in keep and role.upper() != "MAIN":
            to_delete.append(t)

    if not to_delete:
        print("\n✅ Nothing to delete.")
        return

    print(f"\nWill delete {len(to_delete)} theme(s).")
    if not args.yes:
        ans = input("\nProceed? Type 'yes' to confirm: ").strip().lower()
        if ans != "yes":
            print("Aborted.")
            return

    for t in to_delete:
        tid = t["id"]
        result = client.query(DELETE_THEME_MUTATION, {"id": tid})
        errs = result["themeDelete"]["userErrors"]
        if errs:
            print(f"  ✗ {t['name']}: {errs}")
        else:
            print(f"  ✓ deleted {t['name']} ({gid_to_int(tid)})")

    print("\n✅ Cleanup complete.")

if __name__ == "__main__":
    main()
