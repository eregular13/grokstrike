# nmap

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | network — Network Reconnaissance |
| **Binary** | `nmap` ✅ installed |
| **Agent** | network |
| **DVWA-optimized** | True |
| **Lab target** | `aegis-target` |

## Official Purpose
Port scan + service detection

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
nmap -sV -sC -p 80,443,3000,8080 -T4 aegis-target
```

| Metric | Value |
|--------|-------|
| Duration | 7.08s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Open port/service:** open   http       Apache
- **Potential vulnerability signal:** Vulnerable
- **Server version:** Apache/2.4.25

## Full Output Summary
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-24 05:36 +0000
Nmap scan report for aegis-target (172.22.0.2)
Host is up (0.000050s latency).
rDNS record for 172.22.0.2: aegis-target.aegiscontrolplane_default

PORT     STATE  SERVICE    VERSION
80/tcp   open   http       Apache httpd 2.4.25 ((Debian))
| http-title: Login :: Damn Vulnerable Web Application (DVWA) v1.10 *Develop...
|_Requested resource was login.php
| http-robots.txt: 1 disallowed entry 
|_/
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.25 (Debian)
443/tcp  closed https
3000/tcp closed ppp
8080/tcp closed http-proxy
MAC Address: 22:44:33:39:AA:11 (Unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.91 seconds

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `nmap -sV -sC -T4 {host} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `nmap -sV --script vuln` for scripted checks; map all DVWA modules.

---
*GrokStrike v2 — 2026-06-24T05:36:46.266450+00:00*
