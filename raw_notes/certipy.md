# certipy

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | exploit — Exploit Frameworks |
| **Binary** | `certipy` ❌ missing |
| **Agent** | exploit |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
AD CS abuse

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
certipy find -u user@domain -p pass -dc-ip aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.0s |
| Exit code | 127 |
| Effectiveness | **1/10** — Tool binary not installed |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
command not found: certipy
```

## What I Learned / Edge Cases / Gotchas
- `certipy` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `certipy find -u user@domain -p pass -dc-ip {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `certipy --help` and tune `certipy find -u user@domain -p pass -dc-ip {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:53.146000+00:00*
