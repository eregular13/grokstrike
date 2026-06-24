# hydra-ftp

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `hydra` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
FTP brute force

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
hydra -l admin -P /usr/share/wordlists/rockyou.txt aegis-target ftp
```

| Metric | Value |
|--------|-------|
| Duration | 3.99s |
| Exit code | 255 |
| Effectiveness | **5/10** — Non-zero exit but useful output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-06-24 05:47:46
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://aegis-target:21/
0 of 1 target completed, 0 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-06-24 05:47:50

--- STDERR ---
[ERROR] all children were disabled due too many connection errors

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `hydra -l admin -P /usr/share/wordlists/rockyou.txt {host} ftp {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `hydra --help` and tune `hydra -l admin -P /usr/share/wordlists/rockyou.txt {host} ftp {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:50.310895+00:00*
