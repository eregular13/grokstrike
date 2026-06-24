# autorecon

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `autorecon` ❌ missing |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Automated recon pipeline

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
autorecon aegis-target
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
command not found: autorecon
```

## What I Learned / Edge Cases / Gotchas
- `autorecon` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `autorecon {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `autorecon --help` and tune `autorecon {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:36:56.102182+00:00*
