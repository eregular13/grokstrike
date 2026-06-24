# browser-agent

## Tool Name & Category
- **Name:** browser-agent
- **Category:** agent (Autonomous Agent — orchestration and correlation helpers)
- **Binary:** `curl`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Browser capture agent

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
curl -skL aegis-target -o /results/browser_capture.html
```

**Target:** `aegis-target`  
**Duration:** 0.11s | **Exit code:** 0

## Full Output Summary
```

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `curl -skL {web} -o /results/browser_capture.html {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**6/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:40.696859+00:00*
