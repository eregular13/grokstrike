# zap-baseline

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `zap.sh` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
OWASP ZAP baseline

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
zap-baseline.py -t http://aegis-target
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
command not found: zap.sh
```

## What I Learned / Edge Cases / Gotchas
- `zap.sh` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `zap-baseline.py -t {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 600s

## Next Steps for Exploration & Development
Run `zap.sh --help` and tune `zap-baseline.py -t {web} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:43.392606+00:00*
