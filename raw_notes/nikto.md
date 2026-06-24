# nikto

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `nikto` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Web server vulnerability scan

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
nikto -h http://aegis-target -maxtime 360
```

| Metric | Value |
|--------|-------|
| Duration | 325.53s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Nikto/nuclei finding:** [95] /: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cooki
- **Nikto/nuclei finding:** [95] /: Cookie security created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookie
- **Nikto/nuclei finding:** [600050] Apache/2.4.25 appears to be outdated (current is at least 2.4.66).
- **Nikto/nuclei finding:** [013587] /: Suggested security header missing: permissions-policy. See: https://developer.mozilla.org/en-US/docs/Web/HTT
- **Nikto/nuclei finding:** [013587] /: Suggested security header missing: x-content-type-options. See: https://developer.mozilla.org/en-US/docs/Web
- **Nikto/nuclei finding:** [013587] /: Suggested security header missing: referrer-policy. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/H
- **Nikto/nuclei finding:** [013587] /: Suggested security header missing: strict-transport-security. See: https://developer.mozilla.org/en-US/docs/
- **Nikto/nuclei finding:** [013587] /: Suggested security header missing: content-security-policy. See: https://developer.mozilla.org/en-US/docs/We

## Full Output Summary
```
- Nikto v2.6.0
---------------------------------------------------------------------------
+ Target IP:          172.22.0.2
+ Target Hostname:    aegis-target
+ Target Port:        80
+ Platform:           Linux/Unix
+ Start Time:         2026-06-24 05:41:35 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.25 (Debian)
+ [95] /: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ [95] /: Cookie security created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ No CGI Directories found (use '-C all' to force check all possible dirs). CGI tests skipped.
+ [600050] Apache/2.4.25 appears to be outdated (current is at least 2.4.66).
+ [013587] /: Suggested security header missing: permissions-policy. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy
+ [013587] /: Suggested security header missing: x-content-type-options. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options
+ [013587] /: Suggested security header missing: referrer-policy. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
+ [013587] /: Suggested security header missing: strict-transport-security. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
+ [013587] /: Suggested security header missing: content-security-policy. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
+ [750500] /config/: Directory indexing found.
+ [000998] /config/: Configuration information may be available remotely.
+ [750500] /docs/: Directory indexing found.
+ [003584] /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ [006333] /login.php: Admin login page/section found.
+ [007224] /.gitignore: .gitignore file found. It is possible to grasp the directory structure.
+ [007342] /: X-Frame-Options header is deprecated and was replaced with the Content-Security-Policy HTTP header with the frame-ancestors directive. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options
+ [007352] /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ 7799 requests: 16 errors and 16 items reported on the remote host
+ End Time:           2026-06-24 05:47:00 (GMT0) (325 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

--- STDERR ---
+ ERROR: Failed to check for updates: 403

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `nikto -h {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 420s

## Next Steps for Exploration & Development
Pipe to report: `nikto -h URL -Format htm -output /results/nikto.html`.

---
*GrokStrike v2 — 2026-06-24T05:47:00.564367+00:00*
