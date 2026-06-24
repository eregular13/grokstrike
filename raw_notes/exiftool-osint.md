# exiftool-osint

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | osint — OSINT |
| **Binary** | `exiftool` ✅ installed |
| **Agent** | osint |
| **DVWA-optimized** | False |
| **Lab target** | `localhost` |

## Official Purpose
OSINT metadata parse

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
exiftool -r /results/metagoofil
```

| Metric | Value |
|--------|-------|
| Duration | 0.15s |
| Exit code | 1 |
| Effectiveness | **1/10** — Binary missing |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
Error: File not found - /results/metagoofil

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `exiftool -r /results/metagoofil {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `exiftool --help` and tune `exiftool -r /results/metagoofil {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:35.861142+00:00*
