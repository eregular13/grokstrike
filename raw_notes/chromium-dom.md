# chromium-dom

## Tool Name & Category
- **Name:** chromium-dom
- **Category:** browser (Browser Agent — headless rendering, DOM capture, screenshots)
- **Binary:** `chromium`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
DOM dump via headless Chrome

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
chromium --headless --dump-dom http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 0.12s | **Exit code:** 1

## Full Output Summary
```
[14016:14016:0624/051127.609031:ERROR:content/browser/zygote_host/zygote_host_impl_linux.cc:101] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `chromium --headless --dump-dom {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:27.620329+00:00*
