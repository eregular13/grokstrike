# dnsrecon

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | osint — OSINT |
| **Binary** | `dnsrecon` ❌ missing |
| **Agent** | osint |
| **DVWA-optimized** | False |
| **Lab target** | `localhost` |

## Official Purpose
DNS recon

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
dnsrecon -d localhost
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
command not found: dnsrecon
```

## What I Learned / Edge Cases / Gotchas
- `dnsrecon` not found — run `scripts/kali-full-bootstrap.sh`
- Registry template: `dnsrecon -d {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `dnsrecon --help` and tune `dnsrecon -d {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:35.974568+00:00*
