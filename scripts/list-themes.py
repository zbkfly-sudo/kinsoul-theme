#!/usr/bin/env python3
"""List all themes in the store — read-only, no mutations."""
import json, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
env = {}
for line in (ROOT / ".env").read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip()

store = env["SHOPIFY_STORE"]
token = env["SHOPIFY_ADMIN_API_TOKEN"]
live_id = int(env["SHOPIFY_LIVE_THEME_ID"])

query = """{
  themes(first: 50) {
    edges { node { id name role createdAt updatedAt } }
  }
}"""

req = urllib.request.Request(
    f"https://{store}/admin/api/2026-01/graphql.json",
    data=json.dumps({"query": query}).encode(),
    headers={"Content-Type": "application/json", "X-Shopify-Access-Token": token},
    method="POST",
)
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read())

themes = [e["node"] for e in data["data"]["themes"]["edges"]]
themes.sort(key=lambda t: t["createdAt"], reverse=True)

print(f"\nStore: {store}")
print(f"Total themes: {len(themes)}")
print(f"Live theme ID: {live_id}\n")

print(f"{'#':<3} {'Theme ID':<14}  {'Role':<11}  {'Created':<20}  Name")
print("-" * 110)
for i, t in enumerate(themes, 1):
    tid = int(t["id"].rsplit("/", 1)[-1])
    role = t["role"] or ""
    created = t["createdAt"][:19].replace("T", " ")
    mark = "🔒 LIVE" if tid == live_id else "  "
    print(f"{i:<3} {tid:<14}  {role:<11}  {created:<20}  {mark} {t['name']}")

print(f"\n(Nothing deleted — this is a read-only list.)")
