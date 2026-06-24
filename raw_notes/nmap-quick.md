# nmap-quick

## Tool Name & Category
- **Name:** nmap-quick
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `nmap`
- **Agent:** network
- **DVWA-optimized:** True

## Official Purpose
Fast top-port scan

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nmap -F -T4 aegis-target
```

**Target:** `aegis-target`  
**Duration:** 0.75s | **Exit code:** 0

## Full Output Summary
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-24 05:05 +0000
Nmap scan report for aegis-target (172.22.0.2)
Host is up (0.000013s latency).
rDNS record for 172.22.0.2: aegis-target.aegiscontrolplane_default
Not shown: 99 closed tcp ports (reset)
PORT   STATE SERVICE
80/tcp open  http
MAC Address: 22:44:33:39:AA:11 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.65 seconds

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `nmap -F -T4 {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:05:56.064430+00:00*
