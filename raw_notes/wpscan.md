# wpscan

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `wpscan` ❌ missing |
| **Agent** | web |
| **DVWA-optimized** | False |
| **Lab target** | `http://aegis-juice:3000` |

## Official Purpose
WordPress scanner

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
wpscan --url http://aegis-juice:3000 --no-update --enumerate vp --max-threads 2 2>&1 | head -40
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
command not found: wpscan
```

## What I Learned / Edge Cases / Gotchas
- `wpscan` not found — run `scripts/kali-full-bootstrap.sh`
- Juice Shop is a SPA — API endpoints (`/rest`, `/api`) often more fruitful than path brute force
- Registry template: `wpscan --url {web} --enumerate vp,vt {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `wpscan --help` and tune `wpscan --url {web} --enumerate vp,vt {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:40.453485+00:00*
