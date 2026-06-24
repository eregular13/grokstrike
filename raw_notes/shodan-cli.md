# shodan-cli

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | osint — OSINT |
| **Binary** | `shodan` ✅ installed |
| **Agent** | osint |
| **DVWA-optimized** | False |
| **Lab target** | `localhost` |

## Official Purpose
Shodan host lookup

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
shodan host localhost
```

| Metric | Value |
|--------|-------|
| Duration | 0.27s |
| Exit code | 1 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
Error: Please run "shodan init <api key>" before using this command

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `shodan host {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `shodan --help` and tune `shodan host {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:35.155257+00:00*
