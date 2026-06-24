# jwt-tool

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `jwt-tool` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | False |
| **Lab target** | `http://aegis-juice:3000` |

## Official Purpose
JWT testing

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
jwt-tool -t http://aegis-juice:3000
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
command not found: jwt-tool
```

## What I Learned / Edge Cases / Gotchas
- `jwt-tool` not found — run `scripts/kali-full-bootstrap.sh`
- Juice Shop is a SPA — API endpoints (`/rest`, `/api`) often more fruitful than path brute force
- Registry template: `jwt-tool -t {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `jwt-tool --help` and tune `jwt-tool -t {web} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:42.227360+00:00*
