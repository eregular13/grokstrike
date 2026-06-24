# dalfox

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `dalfox` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
XSS scanner

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
dalfox url 'http://aegis-target/vulnerabilities/xss_r/?name=test' --cookie "$(/workspace/dvwa_login.sh http://aegis-target)" --silence
```

| Metric | Value |
|--------|-------|
| Duration | 0.0s |
| Exit code | 127 |
| Effectiveness | **1/10** — Tool binary not installed |

## Key Findings
- See output summary for raw tool data.

## Full Output Summary
```

--- STDERR ---
command not found: dalfox
```

## What I Learned / Edge Cases / Gotchas
- `dalfox` not found — run `scripts/kali-full-bootstrap.sh`
- DVWA requires authenticated session — `/workspace/dvwa_login.sh` sets cookies + security=low
- Registry template: `dalfox url {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Point at Juice Shop search: `dalfox url 'http://aegis-juice:3000/#/search?q=test'`.

---
*GrokStrike v2 — 2026-06-24T05:47:40.774312+00:00*
