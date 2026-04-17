#!/usr/bin/env python3
"""List available Files (shop_images) in the Shopify store via Admin API."""
import json, sys, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
env = {}
for line in (ROOT / ".env").read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip()

store = env["SHOPIFY_STORE"]
token = env["SHOPIFY_ADMIN_API_TOKEN"]

query = """
query {
  files(first: 50) {
    edges {
      node {
        ... on MediaImage {
          id
          alt
          image { url altText }
          preview { image { url } }
        }
        ... on GenericFile {
          id
          alt
          url
        }
      }
    }
  }
}
"""

req = urllib.request.Request(
    f"https://{store}/admin/api/2026-01/graphql.json",
    data=json.dumps({"query": query}).encode(),
    headers={"Content-Type": "application/json", "X-Shopify-Access-Token": token},
    method="POST",
)
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read())

for edge in data["data"]["files"]["edges"]:
    node = edge["node"]
    url = node.get("image", {}).get("url") or node.get("url") or node.get("preview", {}).get("image", {}).get("url")
    if url:
        fname = url.split("/")[-1].split("?")[0]
        print(f"{fname}  → {node.get('id', '')}")
