# patator

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `patator` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Multi-module brute forcer

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
patator http_fuzz url=http://aegis-target method=GET
```

| Metric | Value |
|--------|-------|
| Duration | 1.27s |
| Exit code | 0 |
| Effectiveness | **5/10** — Ran successfully, limited findings |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
05:47:52 patator    INFO - Starting Patator 1.1.0 (https://github.com/lanjelot/patator) with Python-3.13.14 at 2026-06-24 05:47 UTC
05:47:52 patator    INFO -                                                                              
05:47:52 patator    INFO - code size:clen       time | candidate                          |   num | mesg
05:47:52 patator    INFO - -----------------------------------------------------------------------------
05:47:52 patator    INFO - 302  423:0          0.001 |                                    |     1 | HTTP/1.1 302 Found
05:47:53 patator    INFO - Hits/Done/Skip/Fail/Size: 1/1/0/0/1, Avg: 1 r/s, Time: 0h 0m 0s

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `patator http_fuzz url={web} method=GET {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `patator --help` and tune `patator http_fuzz url={web} method=GET {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:53.304965+00:00*
