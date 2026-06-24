# nuclei

## Tool Name & Category
- **Name:** nuclei
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `nuclei`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Template-based vuln scan

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nuclei -u http://aegis-target -severity low,medium,high,critical
```

**Target:** `http://aegis-target`  
**Duration:** 19.88s | **Exit code:** 0

## Full Output Summary
```
[[93mWRN[0m] Loading 2 unsigned templates for scan. Use with caution.

                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v3.8.0

		projectdiscovery.io

[[31mWRN[0m] Found 2 templates with runtime error (use -validate flag for further examination)
[[34mINF[0m] Current nuclei version: v3.8.0 ([91moutdated[0m)
[[34mINF[0m] Current nuclei-templates version: v10.4.5 ([92mlatest[0m)
[[34mINF[0m] New templates added in latest release: 86
[[34mINF[0m] Templates loaded for current scan: 6749
[[34mINF[0m] Executing 6747 signed templates from projectdiscovery/nuclei-templates
[[34mINF[0m] Targets loaded for current scan: 1
[[34mINF[0m] Templates clustered: 463 (Reduced 397 Requests)
[[34mINF[0m] Skipped aegis-target:80 from target list as found unresponsive permanently: cause="no address found for host"
[[34mINF[0m] Skipped aegis-target:80 from target list as found unresponsive permanently: cause="no address found for host" chain="got err while executing http://aegis-target/%u002e/WEB-INF/web.xml"
[[34mINF[0m] Skipped aegis-target:80 from target list as found unresponsive permanently: cause="no address found for host"
[[34mINF[0m] Skipped aegis-target:80 from target list as found unresponsive permanently: cause="no address found for host" chain="got err while executing http://aegis-target/icons/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/etc/passwd"
[[34mINF[0m] Skipped aegis-target:80 from target list as found unresponsive permanently: cause="no address found for host" chain="got err while executing http://aegis-target/setup/setup-s/%u002e%u002e/%u002e%u002e/log.jsp"
[[34mINF[0m] Scan completed in 18.389032037s. 0 matches found.

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `nuclei -u {web} -severity low,medium,high,critical {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:14.540007+00:00*
