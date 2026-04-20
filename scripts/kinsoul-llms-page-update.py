#!/usr/bin/env python3
"""
Kinsoul llms.txt page body rewrite + publish.

Target page: gid://shopify/Page/256119341142
  handle:           llms-txt-kinsoul-energy
  templateSuffix:   llms-txt   -> templates/page.llms-txt.liquid
                                  ({% layout none %}{{ page.content | strip_html }})

Does:
  1. Reads new body from /tmp/llms-page-new-body.md
  2. Snapshots current body + isPublished into scripts/llms-page-rollback-<ts>.json
  3. pageUpdate: body = new markdown; isPublished = true
  4. Appends an entry to scripts/shopify-admin-ops.log

Usage:
  python3 scripts/kinsoul-llms-page-update.py --dry-run   # print diff, no write
  python3 scripts/kinsoul-llms-page-update.py             # apply

Rollback:
  python3 scripts/kinsoul-llms-page-update.py --rollback=scripts/llms-page-rollback-<ts>.json
"""
import sys
import json
import datetime
import difflib
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_PATH = ROOT / "scripts" / "shopify-admin-ops.log"
ROLLBACK_DIR = ROOT / "scripts"
NEW_BODY_PATH = Path("/tmp/llms-page-new-body.md")

API_VERSION = "2026-04"
EXPECTED_STORE = "qr4xym-qi.myshopify.com"
PAGE_GID = "gid://shopify/Page/256119341142"
EXPECTED_HANDLE = "llms-txt-kinsoul-energy"


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
        f.write(f"{ts} | pageUpdate (llms-txt)     | {detail}\n")


def gql(store, token, query, variables):
    endpoint = f"https://{store}/admin/api/{API_VERSION}/graphql.json"
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=payload,
        headers={
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": token,
            "Accept": "application/json",
        }, method="POST",
    )
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
  page(id: $id) {
    id handle title templateSuffix isPublished publishedAt updatedAt
    body bodySummary
  }
}
"""

Q_UPDATE = """
mutation($id: ID!, $page: PageUpdateInput!) {
  pageUpdate(id: $id, page: $page) {
    page { id handle title isPublished publishedAt updatedAt }
    userErrors { code field message }
  }
}
"""


def do_rollback(path, env):
    snapshot = json.loads(Path(path).read_text())
    if snapshot.get("page_id") != PAGE_GID:
        print(f"Rollback file is for a different page ({snapshot.get('page_id')}), aborting.")
        sys.exit(1)
    print(f"Rolling back to snapshot taken at {snapshot.get('taken_at')}")
    print(f"  isPublished was: {snapshot.get('isPublished')}")
    print(f"  body was {len(snapshot.get('body') or '')} chars")
    res = gql(env["SHOPIFY_STORE"], env["SHOPIFY_ADMIN_API_TOKEN"], Q_UPDATE, {
        "id": PAGE_GID,
        "page": {
            "body": snapshot.get("body") or "",
            "isPublished": bool(snapshot.get("isPublished")),
        },
    })
    ue = res["pageUpdate"]["userErrors"]
    if ue:
        print(f"Rollback failed: {ue}")
        sys.exit(2)
    log_op(f"ROLLBACK from={path} status=OK")
    print("Rollback complete.")


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    rollback_arg = next((a for a in args if a.startswith("--rollback=")), None)

    env = load_env()
    store = env.get("SHOPIFY_STORE", "").strip()
    token = env.get("SHOPIFY_ADMIN_API_TOKEN", "").strip()
    if store != EXPECTED_STORE:
        print(f"Refusing: SHOPIFY_STORE={store!r} != {EXPECTED_STORE!r}")
        sys.exit(1)
    if not token.startswith("shpat_"):
        print("Refusing: SHOPIFY_ADMIN_API_TOKEN does not look like shpat_...")
        sys.exit(1)

    if rollback_arg:
        do_rollback(rollback_arg.split("=", 1)[1], env)
        return

    if not NEW_BODY_PATH.exists():
        print(f"Missing new body source: {NEW_BODY_PATH}")
        sys.exit(1)
    new_body = NEW_BODY_PATH.read_text()

    current = gql(store, token, Q_GET, {"id": PAGE_GID})["page"]
    if current is None:
        print("Page not found. Aborting.")
        sys.exit(1)
    if current.get("handle") != EXPECTED_HANDLE:
        print(f"Handle mismatch: got {current.get('handle')!r}, expected {EXPECTED_HANDLE!r}")
        sys.exit(1)

    old_body = current.get("body") or ""
    print(f"Page:         {current['title']!r}")
    print(f"Handle:       {current['handle']}")
    print(f"Template:     {current.get('templateSuffix')}")
    print(f"Was published: {current.get('isPublished')}  updatedAt={current.get('updatedAt')}")
    print(f"Old body:     {len(old_body)} chars")
    print(f"New body:     {len(new_body)} chars")
    print()
    print("--- UNIFIED DIFF (first 150 lines) ---")
    diff = list(difflib.unified_diff(
        old_body.splitlines(keepends=False),
        new_body.splitlines(keepends=False),
        fromfile="old_body", tofile="new_body", lineterm="",
    ))
    for line in diff[:150]:
        print(line)
    if len(diff) > 150:
        print(f"... ({len(diff) - 150} more diff lines) ...")
    print()

    if dry_run:
        print("DRY RUN — no changes applied.")
        return

    # Snapshot
    ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    snap_path = ROLLBACK_DIR / f"llms-page-rollback-{ts}.json"
    snap_path.write_text(json.dumps({
        "taken_at": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "page_id": current["id"],
        "handle": current["handle"],
        "title": current["title"],
        "templateSuffix": current.get("templateSuffix"),
        "isPublished": current.get("isPublished"),
        "publishedAt": current.get("publishedAt"),
        "updatedAt": current.get("updatedAt"),
        "body": old_body,
    }, indent=2))
    print(f"Snapshot: {snap_path}")

    # Apply
    res = gql(store, token, Q_UPDATE, {
        "id": PAGE_GID,
        "page": {"body": new_body, "isPublished": True},
    })
    out = res["pageUpdate"]
    ue = out.get("userErrors") or []
    if ue:
        print(f"userErrors: {ue}")
        log_op(f"FAIL handle={current['handle']} errors={ue}")
        sys.exit(2)
    page_after = out["page"]
    print(f"OK  isPublished={page_after['isPublished']}  publishedAt={page_after.get('publishedAt')}  updatedAt={page_after.get('updatedAt')}")
    log_op(
        f"handle={current['handle']} id={current['id']} "
        f"body_len={len(new_body)} isPublished={page_after['isPublished']} "
        f"rollback_file={snap_path.name} status=OK user_confirmed=true"
    )


if __name__ == "__main__":
    main()
