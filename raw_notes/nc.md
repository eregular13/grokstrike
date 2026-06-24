# nc

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `nc` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | True |
| **Lab target** | `aegis-target` |

## Official Purpose
Port connectivity check

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
nc -zv aegis-target 80 443 3000 8080 2>&1
```

| Metric | Value |
|--------|-------|
| Duration | 0.1s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
DNS fwd/rev mismatch: aegis-target != aegis-target.aegiscontrolplane_default
aegis-target [172.22.0.2] 80 (http) open

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `nc -zv {host} 80 443 8080 {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 30s

## Next Steps for Exploration & Development
Run `nc --help` and tune `nc -zv {host} 80 443 8080 {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:41:15.104568+00:00*
