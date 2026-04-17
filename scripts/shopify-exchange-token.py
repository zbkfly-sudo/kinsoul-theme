#!/usr/bin/env python3
"""
Exchange Shopify Custom App Client ID + Client Secret for a 24h Access Token.

Per Shopify docs (2026 Dev Dashboard custom app flow):
  https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant

The returned access_token is valid for 24 hours and can be used as the
X-Shopify-Access-Token header for Admin API calls.

Usage:
  python3 scripts/shopify-exchange-token.py
  → prints access_token to stdout
  → writes it to .env as SHOPIFY_ADMIN_API_TOKEN (overwrites prev value)

Reads from .env:
  SHOPIFY_STORE
  SHOPIFY_ADMIN_CLIENT_ID        — Dev Dashboard app's Client ID
  SHOPIFY_ADMIN_CLIENT_SECRET    — shpss_… value

If SHOPIFY_ADMIN_CLIENT_ID missing but SHOPIFY_ADMIN_API_TOKEN=shpss_…,
treats the shpss_ value as client_secret and prompts for Client ID.
"""

import json
import os
import sys
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"

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

def save_env_key(key, value):
    """Update one key in .env, preserving others."""
    lines = ENV_PATH.read_text().splitlines()
    found = False
    new_lines = []
    for line in lines:
        if line.strip().startswith(f"{key}="):
            new_lines.append(f"{key}={value}")
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(f"{key}={value}")
    ENV_PATH.write_text("\n".join(new_lines) + "\n")

def main():
    env = load_env()
    store = env.get("SHOPIFY_STORE", "").strip()
    client_id = env.get("SHOPIFY_ADMIN_CLIENT_ID", "").strip()
    client_secret = env.get("SHOPIFY_ADMIN_CLIENT_SECRET", "").strip()

    # Convenience: if user put shpss_ as SHOPIFY_ADMIN_API_TOKEN by mistake,
    # treat it as the client secret.
    if not client_secret:
        fallback = env.get("SHOPIFY_ADMIN_API_TOKEN", "").strip()
        if fallback.startswith("shpss_"):
            client_secret = fallback

    if not store:
        print("❌ SHOPIFY_STORE missing from .env")
        sys.exit(1)

    if not client_id:
        print("""
❌ SHOPIFY_ADMIN_CLIENT_ID missing from .env

   Add to .env:
     SHOPIFY_ADMIN_CLIENT_ID=<the 32-char Client ID from Dev Dashboard>

   Find it at: Dev Dashboard → your app → Settings → Credentials → Client ID
""")
        sys.exit(1)

    if not client_secret:
        print("""
❌ SHOPIFY_ADMIN_CLIENT_SECRET missing from .env

   Add to .env:
     SHOPIFY_ADMIN_CLIENT_SECRET=shpss_<the secret from Dev Dashboard>
""")
        sys.exit(1)

    # Per Shopify docs: form-urlencoded, NOT JSON
    url = f"https://{store}/admin/oauth/access_token"
    payload = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode("utf-8")

    print(f"Store: {store}")
    print(f"Client ID: {client_id[:8]}…{client_id[-4:]} (length {len(client_id)})")
    print(f"Client Secret: shpss_…{client_secret[-4:]} (length {len(client_secret)})")
    print(f"POST {url}")
    print(f"Content-Type: application/x-www-form-urlencoded")
    print(f"grant_type=client_credentials")
    print()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"❌ HTTP {e.code}")
        print(body[:2000])
        print("\nTroubleshooting:")
        print("  • 'application_cannot_be_found' → Client ID typo or app installed on wrong store")
        print("  • 'invalid_client' → Client Secret wrong, or grant not enabled on app")
        print("  • 404 → endpoint URL wrong (check SHOPIFY_STORE value)")
        sys.exit(2)

    access_token = data.get("access_token")
    scope = data.get("scope", "")
    expires = data.get("expires_in", "?")

    if not access_token:
        print("❌ Unexpected response (no access_token field):")
        print(json.dumps(data, indent=2))
        sys.exit(2)

    print("✅ SUCCESS")
    print(f"   access_token: {access_token[:8]}…{access_token[-4:]}")
    print(f"   scope:        {scope}")
    print(f"   expires_in:   {expires} seconds (~24h)")
    print()

    save_env_key("SHOPIFY_ADMIN_API_TOKEN", access_token)
    print(f"✅ Wrote access_token to {ENV_PATH} as SHOPIFY_ADMIN_API_TOKEN")
    print()
    print("Now you can run:")
    print("   python3 scripts/kinsoul-admin-setup.py --dry-run")

if __name__ == "__main__":
    main()
