# nikto

## Tool Name & Category
- **Name:** nikto
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `nikto`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Web server vulnerability scan

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nikto -h http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** ~327s (full run) | **Exit code:** 0 (supplemental deep scan)

## Full Output Summary
```
- Nikto v2.6.0
+ Target IP:          172.22.0.2
+ Target Hostname:    aegis-target
+ Target Port:        80
+ Server: Apache/2.4.25 (Debian)
+ [95] /: Cookie PHPSESSID created without the httponly flag
+ [95] /: Cookie security created without the httponly flag
+ [600050] Apache/2.4.25 appears to be outdated (current is at least 2.4.66)
+ [013587] /: Suggested security header missing: referrer-policy
+ [013587] /: Suggested security header missing: content-security-policy
+ [013587] /: Suggested security header missing: x-content-type-options
+ [013587] /: Suggested security header missing: permissions-policy
+ [013587] /: Suggested security header missing: strict-transport-security
+ [750500] /config/: Directory indexing found
+ [000998] /config/: Configuration information may be available remotely
+ [750500] /docs/: Directory indexing found
+ [003584] /icons/README: Apache default file found
+ [006333] /login.php: Admin login page/section found
+ [007224] /.gitignore: .gitignore file found
```

## What I Learned / Edge Cases / Gotchas
- **Batch run timed out at 120s** — nikto needs 5+ minutes for full DVWA scan; use `-Tuning` or `-maxtime` for lab runs
- Confirms gobuster findings: `/config/`, `/docs/` have directory indexing enabled
- Cookie flags and missing security headers are high-value DVWA learning points
- Apache 2.4.25 EOL version flagged — aligns with nmap service detection
- Registry template: `nikto -h {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**9/10** — Excellent DVWA coverage when given adequate runtime; finds misconfigs gobuster alone misses

## Recommended Safe Parameters for Learning Labs
- `--maxtime 600` or allow 5+ min runtime for full scan
- `-Tuning 123456789` to focus specific test categories
- `--batch --risk=1 --level=1` for injection tools; `-T4` for nmap; target=http://aegis-target only; no destructive flags
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:10:54.655659+00:00*
