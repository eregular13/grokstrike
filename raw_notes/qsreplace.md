# qsreplace

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `qsreplace` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Query param replacement

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
echo http://aegis-target | qsreplace FUZZ
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
command not found: qsreplace
```

## What I Learned / Edge Cases / Gotchas
- `qsreplace` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `echo {web} | qsreplace FUZZ {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 30s

## Next Steps for Exploration & Development
Run `qsreplace --help` and tune `echo {web} | qsreplace FUZZ {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:43.829532+00:00*
