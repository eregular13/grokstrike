# impacket-wmiexec

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | exploit — Exploit Frameworks |
| **Binary** | `wmiexec` ❌ missing |
| **Agent** | exploit |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
WMI command exec

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
wmiexec.py user:pass@aegis-target
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
command not found: wmiexec
```

## What I Learned / Edge Cases / Gotchas
- `wmiexec` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `wmiexec.py user:pass@{host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `wmiexec --help` and tune `wmiexec.py user:pass@{host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:52.834665+00:00*
