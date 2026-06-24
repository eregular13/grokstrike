# metagoofil

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | osint — OSINT |
| **Binary** | `metagoofil` ❌ missing |
| **Agent** | osint |
| **DVWA-optimized** | False |
| **Lab target** | `localhost` |

## Official Purpose
Document metadata harvest

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
metagoofil -d localhost -t pdf,doc,xls -l 10 -o /results/metagoofil
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
command not found: metagoofil
```

## What I Learned / Edge Cases / Gotchas
- `metagoofil` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `metagoofil -d {host} -t pdf,doc,xls -l 10 -o /results/metagoofil {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `metagoofil --help` and tune `metagoofil -d {host} -t pdf,doc,xls -l 10 -o /results/metagoofil {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:35.609797+00:00*
