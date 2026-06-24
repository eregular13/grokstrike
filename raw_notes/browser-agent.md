# browser-agent

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | agent — Autonomous Agents |
| **Binary** | `curl` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `aegis-target` |

## Official Purpose
Browser capture agent

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
curl -skL http://aegis-target -o /results/browser_capture.html && wc -c /results/browser_capture.html
```

| Metric | Value |
|--------|-------|
| Duration | 0.12s |
| Exit code | 0 |
| Effectiveness | **7/10** — Good lab signal |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
1523 /results/browser_capture.html

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `curl -skL {web} -o /results/browser_capture.html {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `curl --help` and tune `curl -skL {web} -o /results/browser_capture.html {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:54.532190+00:00*
