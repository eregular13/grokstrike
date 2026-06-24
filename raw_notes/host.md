# host

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `host` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
DNS host lookup

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
host -a aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 3.96s |
| Exit code | 1 |
| Effectiveness | **1/10** — Binary missing |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Trying "aegis-target"
Host aegis-target not found: 3(NXDOMAIN)
Received 30 bytes from 127.0.0.11#53 in 3844 ms
Received 30 bytes from 127.0.0.11#53 in 3844 ms

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `host -a {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 30s

## Next Steps for Exploration & Development
Run `host --help` and tune `host -a {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:41:14.910558+00:00*
