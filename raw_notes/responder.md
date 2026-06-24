# responder

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `responder` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
LLMNR/NBT-NS poisoner

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
timeout 30 responder -I eth0 -A
```

| Metric | Value |
|--------|-------|
| Duration | 30.12s |
| Exit code | 124 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `timeout 30 responder -I eth0 -A {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `responder --help` and tune `timeout 30 responder -I eth0 -A {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:41:02.035281+00:00*
