# fierce

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `fierce` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
DNS reconnaissance

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
fierce -dns aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 0.35s |
| Exit code | 2 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
usage: fierce [-h] [--domain DOMAIN] [--connect] [--wide]
              [--traverse TRAVERSE] [--search SEARCH [SEARCH ...]]
              [--range RANGE] [--delay DELAY]
              [--subdomains SUBDOMAINS [SUBDOMAINS ...] |
              --subdomain-file SUBDOMAIN_FILE]
              [--dns-servers DNS_SERVERS [DNS_SERVERS ...] |
              --dns-file DNS_FILE] [--tcp]
fierce: error: unrecognized arguments: -dns aegis-target

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `fierce -dns {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `fierce --help` and tune `fierce -dns {host} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:37:15.495715+00:00*
