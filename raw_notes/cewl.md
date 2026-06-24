# cewl

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `cewl` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Custom wordlist generator

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
cewl http://aegis-target -w /workspace/cewl.txt
```

| Metric | Value |
|--------|-------|
| Duration | 0.38s |
| Exit code | 0 |
| Effectiveness | **7/10** — Good lab signal |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
CeWL 6.2.1 (More Fixes) Robin Wood (robin@digi.ninja) (https://digi.ninja/)

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `cewl {web} -w /workspace/cewl.txt {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `cewl --help` and tune `cewl {web} -w /workspace/cewl.txt {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:54.281999+00:00*
