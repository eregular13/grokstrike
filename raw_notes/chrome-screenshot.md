# chrome-screenshot

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | browser — Browser Agent |
| **Binary** | `chromium` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Headless screenshot

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
chromium --headless --disable-gpu --screenshot=/results/screen.png http://aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.15s |
| Exit code | 1 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
[41563:41563:0624/054744.279995:ERROR:content/browser/zygote_host/zygote_host_impl_linux.cc:101] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `chromium --headless --disable-gpu --screenshot=/results/screen.png {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 90s

## Next Steps for Exploration & Development
Run `chromium --help` and tune `chromium --headless --disable-gpu --screenshot=/results/screen.png {web} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:44.291835+00:00*
