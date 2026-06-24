# rubeus

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | exploit — Exploit Frameworks |
| **Binary** | `Rubeus` ❌ missing |
| **Agent** | exploit |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Kerberos abuse

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
echo 'Rubeus Windows-only'
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
command not found: Rubeus
```

## What I Learned / Edge Cases / Gotchas
- `Rubeus` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `echo 'Rubeus Windows-only' {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 10s

## Next Steps for Exploration & Development
Run `Rubeus --help` and tune `echo 'Rubeus Windows-only' {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:53.038495+00:00*
