# gobuster

## Tool Name & Category
- **Name:** gobuster
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `gobuster`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Directory brute force

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
gobuster dir -u http://aegis-target -w /usr/share/wordlists/dirb/common.txt -q
```

**Target:** `http://aegis-target`  
**Duration:** 2.01s | **Exit code:** 0 (re-run after `apt install wordlists seclists`)

## Full Output Summary
```
.hta                 (Status: 403) [Size: 291]
.htaccess            (Status: 403) [Size: 296]
.htpasswd            (Status: 403) [Size: 296]
config               (Status: 301) [Size: 313] [--> http://aegis-target/config/]
docs                 (Status: 301) [Size: 311] [--> http://aegis-target/docs/]
external             (Status: 301) [Size: 315] [--> http://aegis-target/external/]
favicon.ico          (Status: 200) [Size: 1406]
index.php            (Status: 302) [Size: 0] [--> login.php]
php.ini              (Status: 200) [Size: 148]
phpinfo.php          (Status: 302) [Size: 0] [--> login.php]
robots.txt           (Status: 200) [Size: 26]
server-status        (Status: 403) [Size: 300]
```

## What I Learned / Edge Cases / Gotchas
- **Initial run failed:** Kali bootstrap omitted `wordlists` package — `dirb/common.txt` missing
- **Fix:** `apt install wordlists seclists` then re-run
- DVWA redirects unauthenticated requests to `login.php` (302 on index/phpinfo)
- Registry template: `gobuster dir -u {web} -w /usr/share/wordlists/dirb/common.txt -q {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**9/10** — Excellent directory discovery on DVWA after wordlists installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:14.635137+00:00*
