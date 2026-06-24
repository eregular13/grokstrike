# dig

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `dig` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
DNS query

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
dig aegis-target ANY +noall +answer
```

| Metric | Value |
|--------|-------|
| Duration | 4.07s |
| Exit code | 0 |
| Effectiveness | **5/10** — Ran successfully, limited findings |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `dig {host} ANY +noall +answer {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 30s

## Next Steps for Exploration & Development
Run `dig --help` and tune `dig {host} ANY +noall +answer {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:41:10.864778+00:00*
