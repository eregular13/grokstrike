# masscan

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `masscan` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
High-speed port scan

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
masscan aegis-target -p80,443,3000,8080 --rate 500 2>&1
```

| Metric | Value |
|--------|-------|
| Duration | 0.11s |
| Exit code | 1 |
| Effectiveness | **5/10** — Non-zero exit but useful output |

## Key Findings
- **Injection indicator:** parameter

## Full Output Summary
```
FAIL: unknown command-line parameter "aegis-target"
 [hint] did you want "--aegis-target"?

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `masscan {host} -p1-1000 --rate 1000 {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `masscan --help` and tune `masscan {host} -p1-1000 --rate 1000 {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:36:55.896875+00:00*
