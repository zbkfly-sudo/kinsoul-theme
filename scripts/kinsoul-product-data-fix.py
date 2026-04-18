#!/usr/bin/env python3
"""
Kinsoul Product Data Fix — one-shot correction of Obsidian / Aura / Soleil data.

Runs against Shopify GraphQL Admin API (2026-04) to correct:
  1. Obsidian: rutilated → tourmalinated quartz (body_html + stone_type metafield)
  2. Aura: "8 gemstones" → "8 from a palette of 12" (body_html + stone_type metafield)
  3. Soleil: add Amethyst to stone_type metafield + Freshwater Round Pearls pearl_type +
     rewrite body_html to include round pearls

Reads from .env:
  SHOPIFY_STORE
  SHOPIFY_ADMIN_API_TOKEN

Rollback:
  Before applying, this script reads existing values and writes them to
  scripts/metafield-rollback-<timestamp>.json. If something goes wrong,
  you can re-run with --rollback=<file> to restore.

Idempotent — if product descriptions already match target, skipped.

Usage:
  python3 scripts/kinsoul-product-data-fix.py --dry-run   # show what will change
  python3 scripts/kinsoul-product-data-fix.py             # apply changes
  python3 scripts/kinsoul-product-data-fix.py --rollback=scripts/metafield-rollback-*.json
"""

import json
import sys
import datetime
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "scripts" / "shopify-admin-ops.log"
ROLLBACK_DIR = ROOT / "scripts"
API_VERSION = "2026-04"
EXPECTED_STORE = "qr4xym-qi.myshopify.com"


def log_op(op, detail):
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


# ---------- Target data per product ----------
# Product handles from CLAUDE.md § 1.3
PRODUCT_HANDLES = {
    "obsidian": "mozhu-persian-agate-baroque-pearl-bracelet",
    "aura":     "aura-balance-bracelet-baroque-pearl-crystal-mixed-gemstones",
    "soleil":   "zining-brazilian-yellow-quartz-clear-quartz-amethyst-bracelet",
}

# New product descriptions (from PRODUCT-DESCRIPTIONS.md, already corrected in that file)
NEW_BODIES = {
    "obsidian": """<p>Obsidian is built around deep black agate paired with tourmalinated quartz — clear stones threaded with fine black needle-like inclusions, as though nature's brush strokes had been caught and frozen in crystal. Soft grey freshwater rice pearls run between them, adding a quiet warmth to the darker stones, with a single baroque pearl anchored at the center. A small S925 sterling silver bar on the strand carries our maker's mark. The whole piece is held on a single fine elastic cord — slip it on, no clasp.</p>
<p>This is the piece that gets worn the most often. It works against bare wrists in summer, slides cleanly under a long sleeve, and reads as quietly intentional with everything from a white tee to a tailored jacket. It's also the one we hear about from people who don't usually wear jewelry — the weight feels grounding, they say, in a way they didn't expect.</p>
<p>In many traditions, black agate is carried for inner resolve and quiet protection — strength that doesn't need to announce itself. Because each agate is cut from natural rough, your stones will have their own pattern of black, charcoal, and faint translucent edges. No two Obsidians are alike.</p>""",
    "aura":     """<p>Aura is a quiet harmony of natural stones — warm tones and cool, opaque and translucent, dense and luminous — anchored by a single large baroque saltwater pearl at the heart of the bracelet. Eight stones are selected by hand for each piece from our curated palette of twelve: tiger's eye, lapis lazuli, amethyst, citrine, amazonite, clear quartz, tourmalinated quartz, red agate, prehnite, grey agate, blue apatite, and small agate accent beads. Each carries its own quiet tradition of grounding, clarity, protection, or wisdom. Worn together, they become something greater than any single stone — a small spectrum of balance, threaded with our S925 silver maker's mark, all held on a single fine elastic cord with no clasp.</p>
<p>On the wrist, Aura has presence without weight. The baroque pearl shifts naturally toward the inside of the wrist as you move — a small unexpected pleasure each time you turn your hand. Pair it with a single neutral piece or wear it alone; it's the kind of bracelet that makes everything else around it feel quieter.</p>
<p>Because every stone is selected by hand and the exact arrangement follows the natural shape of each piece, no two Auras are alike. Yours is one of one.</p>""",
    "soleil":   """<p>Soleil is the warmest piece in the collection: Brazilian citrine at the center, framed by clear quartz tips and deep amethyst rounds toward the ends, threaded with small freshwater round pearls from Zhuji, China. The citrine's golden hue comes from trace iron within the crystal itself, which means every stone is a slightly different shade of sunlight: pale honey, deep amber, soft butter. A small S925 sterling silver bar on the strand carries our maker's mark, all held together on a single fine elastic cord — no clasp.</p>
<p>Worn, Soleil is the lightest piece in the collection — the one that disappears against the wrist for a moment and then catches the light when you reach for something. It pairs naturally with summer fabrics, gold accents, and bare skin, and works just as well as a quiet anchor against winter knits.</p>
<p>Citrine has been carried for centuries as a symbol of optimism, creative energy, and abundance — a small sun for the wrist. Paired with clear quartz, amethyst, and freshwater round pearls, Soleil is warmth meeting clarity meeting calm. The natural variation in the citrine means your Soleil will have its own particular shade — and that's the point.</p>""",
}

# Metafield values to set
METAFIELD_TARGETS = {
    "obsidian": [
        {"namespace": "custom", "key": "stone_type", "type": "single_line_text_field",
         "value": "Black Agate, Tourmalinated Quartz"},
        {"namespace": "custom", "key": "pearl_type", "type": "single_line_text_field",
         "value": "Grey Freshwater Rice Pearls (8mm) + Baroque Pearl"},
    ],
    "aura": [
        {"namespace": "custom", "key": "stone_type", "type": "single_line_text_field",
         "value": "8 natural stones selected from a curated palette of 12: Tiger's Eye, Lapis Lazuli, Amethyst, Citrine, Amazonite, Clear Quartz, Tourmalinated Quartz, Red Agate, Prehnite, Grey Agate, Blue Apatite, Agate Accent Beads"},
        {"namespace": "custom", "key": "pearl_type", "type": "single_line_text_field",
         "value": "Large Baroque Saltwater Pearl (Australia)"},
    ],
    "soleil": [
        {"namespace": "custom", "key": "stone_type", "type": "single_line_text_field",
         "value": "Brazilian Citrine, Clear Quartz, Amethyst"},
        {"namespace": "custom", "key": "pearl_type", "type": "single_line_text_field",
         "value": "Freshwater Round Pearls (Zhuji, China)"},
    ],
}


# ---------- GraphQL ops ----------

GET_PRODUCT_QUERY = """
query getProduct($handle: String!) {
  productByHandle(handle: $handle) {
    id
    handle
    title
    descriptionHtml
    metafields(first: 20, namespace: "custom") {
      edges { node { id namespace key type value } }
    }
  }
}
"""

PRODUCT_UPDATE_MUTATION = """
mutation productUpdate($input: ProductInput!) {
  productUpdate(input: $input) {
    product { id handle descriptionHtml }
    userErrors { field message }
  }
}
"""

METAFIELDS_SET_MUTATION = """
mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { id namespace key value type ownerType }
    userErrors { field message }
  }
}
"""


def fetch_current_state(client):
    state = {}
    for slug, handle in PRODUCT_HANDLES.items():
        result = client.query(GET_PRODUCT_QUERY, {"handle": handle})
        p = result.get("productByHandle")
        if not p:
            print(f"  ✗ {slug:<10} (handle={handle}) — PRODUCT NOT FOUND")
            continue
        existing_metafields = {}
        for edge in p["metafields"]["edges"]:
            m = edge["node"]
            existing_metafields[f"{m['namespace']}.{m['key']}"] = m
        state[slug] = {
            "id": p["id"],
            "handle": p["handle"],
            "title": p["title"],
            "descriptionHtml": p["descriptionHtml"],
            "metafields": existing_metafields,
        }
    return state


def write_rollback_snapshot(state):
    ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    path = ROLLBACK_DIR / f"metafield-rollback-{ts}.json"
    snapshot = {}
    for slug, s in state.items():
        snapshot[slug] = {
            "product_id": s["id"],
            "handle": s["handle"],
            "descriptionHtml": s["descriptionHtml"],
            "metafields": {k: {"value": m["value"], "type": m["type"]}
                           for k, m in s["metafields"].items()},
        }
    path.write_text(json.dumps(snapshot, indent=2))
    print(f"  ↪ rollback snapshot saved to {path}")
    return path


def apply_product_fixes(client, state, dry_run):
    print("\n─── Step · Applying product fixes ─────────────────────────")

    for slug, s in state.items():
        pid = s["id"]
        target_body = NEW_BODIES[slug]
        current_body = s["descriptionHtml"] or ""

        # 1. body_html
        body_needs_update = current_body.strip() != target_body.strip()
        if body_needs_update:
            if dry_run:
                print(f"  · {slug:<10} body_html would be updated (len {len(current_body)} → {len(target_body)})")
            else:
                result = client.query(PRODUCT_UPDATE_MUTATION, {
                    "input": {"id": pid, "descriptionHtml": target_body}
                })
                errs = result["productUpdate"]["userErrors"]
                if errs:
                    print(f"  ✗ {slug:<10} body_html update failed: {errs}")
                    log_op("productUpdate", f"handle={s['handle']} | field=descriptionHtml | status=FAILED | errors={errs}")
                else:
                    print(f"  ✓ {slug:<10} body_html updated")
                    log_op("productUpdate", f"handle={s['handle']} | field=descriptionHtml | status=OK")
        else:
            print(f"  · {slug:<10} body_html already matches — skipping")

        # 2. metafields
        targets = METAFIELD_TARGETS[slug]
        metafields_batch = []
        for t in targets:
            key = f"{t['namespace']}.{t['key']}"
            existing = s["metafields"].get(key)
            needs_update = existing is None or existing["value"] != t["value"]
            if needs_update:
                if dry_run:
                    cur = existing["value"][:40] + "..." if existing else "(not set)"
                    new = t["value"][:40] + "..." if len(t["value"]) > 40 else t["value"]
                    print(f"  · {slug:<10} {key:<18} would be updated:  {cur}  →  {new}")
                else:
                    metafields_batch.append({
                        "ownerId": pid,
                        "namespace": t["namespace"],
                        "key": t["key"],
                        "type": t["type"],
                        "value": t["value"],
                    })
            else:
                print(f"  · {slug:<10} {key:<18} already matches — skipping")

        if metafields_batch and not dry_run:
            result = client.query(METAFIELDS_SET_MUTATION, {"metafields": metafields_batch})
            errs = result["metafieldsSet"]["userErrors"]
            if errs:
                print(f"  ✗ {slug:<10} metafieldsSet failed: {errs}")
                log_op("metafieldsSet", f"handle={s['handle']} | status=FAILED | errors={errs}")
            else:
                count = len(result["metafieldsSet"]["metafields"])
                print(f"  ✓ {slug:<10} set {count} metafields")
                log_op("metafieldsSet", f"handle={s['handle']} | count={count} | status=OK")


# ---------- Rollback ----------

def rollback(client, snapshot_path):
    if not Path(snapshot_path).exists():
        print(f"❌ snapshot file not found: {snapshot_path}")
        sys.exit(1)
    snapshot = json.loads(Path(snapshot_path).read_text())

    print(f"\n─── Rollback from {snapshot_path} ──────────────────────────")
    for slug, s in snapshot.items():
        pid = s["product_id"]
        print(f"  · restoring {slug:<10} ({s['handle']})")

        # body_html
        result = client.query(PRODUCT_UPDATE_MUTATION, {
            "input": {"id": pid, "descriptionHtml": s["descriptionHtml"]}
        })
        errs = result["productUpdate"]["userErrors"]
        if errs:
            print(f"    ✗ body_html restore failed: {errs}")
        else:
            print(f"    ✓ body_html restored")

        # metafields
        batch = []
        for key, m in s["metafields"].items():
            ns, k = key.split(".", 1)
            batch.append({
                "ownerId": pid,
                "namespace": ns,
                "key": k,
                "type": m["type"],
                "value": m["value"],
            })
        if batch:
            result = client.query(METAFIELDS_SET_MUTATION, {"metafields": batch})
            errs = result["metafieldsSet"]["userErrors"]
            if errs:
                print(f"    ✗ metafields restore failed: {errs}")
            else:
                print(f"    ✓ restored {len(batch)} metafields")

    log_op("ROLLBACK", f"snapshot={snapshot_path}")


# ---------- Main ----------

def main():
    dry_run = "--dry-run" in sys.argv
    rollback_args = [a for a in sys.argv if a.startswith("--rollback=")]

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

    print(f"Store: {store}")
    print(f"API:   {API_VERSION}")

    client = ShopifyAdmin(store, token)

    if rollback_args:
        snapshot_path = rollback_args[0].split("=", 1)[1]
        rollback(client, snapshot_path)
        print("\n✅ Rollback complete.")
        return

    if dry_run:
        print("MODE:  dry-run (no writes)")
    else:
        print("MODE:  LIVE (will write to Shopify)")

    print("\n─── Fetching current state ─────────────────────────────────")
    state = fetch_current_state(client)

    if not state:
        print("❌ No products resolved. Check handles.")
        sys.exit(1)

    if not dry_run:
        print("\n─── Writing rollback snapshot ──────────────────────────────")
        write_rollback_snapshot(state)

    apply_product_fixes(client, state, dry_run)

    print("\n✅ Done.")
    if dry_run:
        print("\nThis was a dry-run. To actually apply:")
        print("  python3 scripts/kinsoul-product-data-fix.py")
    else:
        print("\nVerify at:")
        for slug, handle in PRODUCT_HANDLES.items():
            print(f"  https://www.kinsoulenergy.com/products/{handle}")


if __name__ == "__main__":
    main()
