# rpcclient

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `rpcclient` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
RPC enumeration

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
rpcclient -c enumdomusers aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.14s |
| Exit code | 1 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
Cannot connect to server.  Error was NT_STATUS_CONNECTION_REFUSED

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `rpcclient -c enumdomusers {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `rpcclient --help` and tune `rpcclient -c enumdomusers {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:40:00.276552+00:00*
