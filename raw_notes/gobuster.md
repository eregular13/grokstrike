# gobuster

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `gobuster` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Directory brute force

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
gobuster dir -u http://aegis-target -w /usr/share/wordlists/dirb/common.txt -q --no-error
```

| Metric | Value |
|--------|-------|
| Duration | 2.86s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **HTTP discovery:** Status: 403
- **HTTP discovery:** Status: 403
- **HTTP discovery:** Status: 403
- **HTTP discovery:** Status: 301
- **HTTP discovery:** Status: 301
- **HTTP discovery:** Status: 301
- **HTTP discovery:** Status: 200
- **HTTP discovery:** Status: 302

## Full Output Summary
```
.hta                 (Status: 403) [Size: 291]
.htpasswd            (Status: 403) [Size: 296]
.htaccess            (Status: 403) [Size: 296]
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
- Executed successfully in isolated lab
- Registry template: `gobuster dir -u {web} -w /usr/share/wordlists/dirb/common.txt -q {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Try `/usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt` for deeper enum.

---
*GrokStrike v2 — 2026-06-24T05:47:16.828635+00:00*
