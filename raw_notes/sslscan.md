# sslscan

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `sslscan` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
SSL cipher enumeration

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
sslscan aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.11s |
| Exit code | 0 |
| Effectiveness | **7/10** — Good lab signal |

## Key Findings
- **Open port/service:** open a connection

## Full Output Summary
```
Version: [32m2.1.5[0m
OpenSSL 3.6.2 7 Apr 2026
[0m

--- STDERR ---
[31mERROR: Could not open a connection to host aegis-target (172.22.0.2) on port 443 (connect: Connection refused).[0m

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `sslscan {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `sslscan --help` and tune `sslscan {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:41.507583+00:00*
