# graphql-voyager

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `graphql-voyager` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | False |
| **Lab target** | `http://aegis-juice:3000` |

## Official Purpose
GraphQL introspection probe

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
curl -sk http://aegis-juice:3000/api/Products 2>&1 | head -30
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
command not found: graphql-voyager
```

## What I Learned / Edge Cases / Gotchas
- `graphql-voyager` not found — run `scripts/kali-full-bootstrap.sh`
- Juice Shop is a SPA — API endpoints (`/rest`, `/api`) often more fruitful than path brute force
- Registry template: `echo 'GraphQL probe' && curl -s {web}/graphql {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `graphql-voyager --help` and tune `echo 'GraphQL probe' && curl -s {web}/graphql {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:44.038300+00:00*
