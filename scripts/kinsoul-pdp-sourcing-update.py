#!/usr/bin/env python3
"""
Kinsoul PDP Sourcing Update — inject province-level origin terms into the
descriptionHtml of all 6 bracelets.

Reads target bodies from /tmp/pdp-new-bodies.json (keyed by brand name, with
id / handle / descriptionHtml). Diffs against live, snapshots the old values
for rollback, then pageUpdate each product.

Rationale (Phase B of GEO strategy):
  Persian red agate → Kerman province (Iran)
  Freshwater pearls → Zhuji, China
  Baroque saltwater pearls → Australia
  Amethyst → Bolivian Andes
  Citrine → Uruguay (fixed from the historical "Brazilian citrine" misnomer)
  Tourmalinated quartz → Brazil
  Black agate → Mexico
  Clear quartz tips → China's East Sea

Each new body preserves the original three-paragraph voice, with sourcing
additions kept short and factual (knowledge base 02-supply-chain.md).

Usage:
  python3 scripts/kinsoul-pdp-sourcing-update.py --dry-run     # show 6 diffs
  python3 scripts/kinsoul-pdp-sourcing-update.py               # apply all
  python3 scripts/kinsoul-pdp-sourcing-update.py --only=Ember  # apply one
  python3 scripts/kinsoul-pdp-sourcing-update.py --rollback=scripts/pdp-sourcing-rollback-<ts>.json
"""
import sys
import json
import difflib
import datetime
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "scripts" / "shopify-admin-ops.log"
ROLLBACK_DIR = ROOT / "scripts"
NEW_BODIES_PATH = Path("/tmp/pdp-new-bodies.json")

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
        f.write(f"{ts} | pdp-sourcing-update       | {detail}\n")


def gql(store, token, query, variables):
    endpoint = f"https://{store}/admin/api/{API_VERSION}/graphql.json"
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=payload,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Access-Token": token,
                 "Accept": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code}: {body[:600]}")
        sys.exit(2)
    if "errors" in data:
        print(f"GraphQL errors: {json.dumps(data['errors'])[:600]}")
        sys.exit(2)
    return data["data"]


Q_GET = """
query($id: ID!) {
  product(id: $id) {
    id handle title descriptionHtml updatedAt
  }
}
"""

Q_UPDATE = """
mutation($input: ProductUpdateInput!) {
  productUpdate(product: $input) {
    product { id handle updatedAt }
    userErrors { field message }
  }
}
"""


def do_rollback(path, env):
    snapshot = json.loads(Path(path).read_text())
    print(f"Rolling back to snapshot: {snapshot.get('taken_at')}")
    store, token = env["SHOPIFY_STORE"], env["SHOPIFY_ADMIN_API_TOKEN"]
    for name, rec in snapshot["products"].items():
        res = gql(store, token, Q_UPDATE, {"input": {
            "id": rec["id"], "descriptionHtml": rec["descriptionHtml"],
        }})
        ue = res["productUpdate"]["userErrors"]
        if ue:
            print(f"  {name}: FAIL {ue}")
            continue
        print(f"  {name}: restored")
        log_op(f"ROLLBACK handle={rec['handle']} from={Path(path).name} status=OK")


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    only = next((a.split("=", 1)[1] for a in args if a.startswith("--only=")), None)
    rollback_arg = next((a for a in args if a.startswith("--rollback=")), None)

    env = load_env()
    if env.get("SHOPIFY_STORE") != EXPECTED_STORE:
        print(f"Refusing: unexpected store")
        sys.exit(1)
    token = env.get("SHOPIFY_ADMIN_API_TOKEN", "")
    if not token.startswith("shpat_"):
        print("Refusing: token prefix wrong")
        sys.exit(1)

    if rollback_arg:
        do_rollback(rollback_arg, env)
        return

    if not NEW_BODIES_PATH.exists():
        print(f"Missing target bodies: {NEW_BODIES_PATH}")
        sys.exit(1)
    targets = json.loads(NEW_BODIES_PATH.read_text())

    if only:
        if only not in targets:
            print(f"--only={only} not in {list(targets)}")
            sys.exit(1)
        targets = {only: targets[only]}

    store = env["SHOPIFY_STORE"]
    snapshot = {
        "taken_at": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "products": {},
    }
    plan = []
    for name, tgt in targets.items():
        live = gql(store, token, Q_GET, {"id": tgt["id"]})["product"]
        if not live:
            print(f"{name}: product not found by id {tgt['id']}")
            sys.exit(1)
        if live["handle"] != tgt["handle"]:
            print(f"{name}: handle mismatch live={live['handle']} target={tgt['handle']}")
            sys.exit(1)
        old = live["descriptionHtml"] or ""
        new = tgt["descriptionHtml"]
        snapshot["products"][name] = {
            "id": live["id"], "handle": live["handle"],
            "descriptionHtml": old, "updatedAt": live["updatedAt"],
        }
        changed = (old != new)
        plan.append((name, live, old, new, changed))

    print("=" * 78)
    print("Phase B — Kinsoul PDP sourcing update")
    print(f"Targets: {len(plan)}  dry-run: {dry_run}")
    print("=" * 78)
    for name, live, old, new, changed in plan:
        print(f"\n--- {name} ({live['handle']}) ---")
        print(f"    old_len={len(old)}  new_len={len(new)}  changed={changed}")
        if not changed:
            print("    [SKIP] identical")
            continue
        diff = list(difflib.unified_diff(
            old.splitlines(), new.splitlines(),
            fromfile=f"{name}_old", tofile=f"{name}_new", lineterm="",
        ))
        # When old/new are single lines, unified_diff hides the content
        # behind "@@ -1 +1 @@". Fall back to printing the full lines.
        if len(diff) <= 3 or all(not ln.startswith(("+", "-")) or ln.startswith(("+++", "---"))
                                  for ln in diff):
            print("    OLD:")
            print("      " + old[:500].replace("\n", "\n      ") + ("..." if len(old) > 500 else ""))
            print("    NEW:")
            print("      " + new[:500].replace("\n", "\n      ") + ("..." if len(new) > 500 else ""))
        else:
            for ln in diff[:60]:
                print("    " + ln)
            if len(diff) > 60:
                print(f"    ... ({len(diff)-60} more diff lines)")

    if dry_run:
        print("\nDRY RUN — no changes applied.")
        return

    # Snapshot
    ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    snap_path = ROLLBACK_DIR / f"pdp-sourcing-rollback-{ts}.json"
    snap_path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False))
    print(f"\nSnapshot: {snap_path}")

    # Apply
    print("\nApplying...")
    for name, live, old, new, changed in plan:
        if not changed:
            print(f"  {name}: skip (no change)")
            continue
        res = gql(store, token, Q_UPDATE, {"input": {
            "id": live["id"], "descriptionHtml": new,
        }})
        out = res["productUpdate"]
        ue = out.get("userErrors") or []
        if ue:
            print(f"  {name}: FAIL {ue}")
            log_op(f"FAIL handle={live['handle']} errors={ue}")
            sys.exit(2)
        p = out["product"]
        print(f"  {name}: OK  updatedAt={p['updatedAt']}")
        log_op(
            f"handle={live['handle']} id={live['id']} "
            f"old_len={len(old)} new_len={len(new)} "
            f"rollback_file={snap_path.name} status=OK user_confirmed=true"
        )


if __name__ == "__main__":
    main()
