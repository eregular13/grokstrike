# nosqlmap

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `nosqlmap` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | False |
| **Lab target** | `http://aegis-juice:3000` |

## Official Purpose
NoSQL injection

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
nosqlmap -u http://aegis-juice:3000
```

| Metric | Value |
|--------|-------|
| Duration | 0.0s |
| Exit code | 127 |
| Effectiveness | **1/10** — Tool binary not installed |

## Key Findings
- **Potential vulnerability signal:** sql

## Full Output Summary
```

--- STDERR ---
command not found: nosqlmap
```

## What I Learned / Edge Cases / Gotchas
- `nosqlmap` not found — run `scripts/kali-full-bootstrap.sh`
- Juice Shop is a SPA — API endpoints (`/rest`, `/api`) often more fruitful than path brute force
- Registry template: `nosqlmap -u {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `nosqlmap --help` and tune `nosqlmap -u {web} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:42.004503+00:00*
