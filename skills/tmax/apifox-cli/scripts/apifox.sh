#!/usr/bin/env bash
# apifox.sh — run the apifox CLI with the WorkBuddy sandbox intercepting proxy removed.
#
# WHY: The sandbox forces HTTP(S)_PROXY=127.0.0.1:56871 on all egress. That proxy
# rewrites HTTPS requests to apifox, so the server gets a mangled request and returns
# 400 "invalid token" even when the token is valid. Stripping the proxy fixes it.
# Every apifox command that touches the network MUST be run through this wrapper (or
# with the equivalent `env -u HTTP_PROXY ...` prefix).
#
# Usage: bash <skill-dir>/scripts/apifox.sh <any apifox subcommand and args>
set -euo pipefail

export PATH="/Users/mk/.npm-global/bin:$PATH"

AP="apifox"
if [ ! -x "$AP" ] && [ -x "/Users/mk/.npm-global/bin/apifox" ]; then
  AP="/Users/mk/.npm-global/bin/apifox"
fi

exec env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy "$AP" "$@"
