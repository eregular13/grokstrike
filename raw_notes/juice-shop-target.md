# Juice Shop Target Profile

## Tool Name & Category
- **Name:** juice-shop-target
- **Category:** web (Secondary Lab Target)
- **Container:** `aegis-juice` on `aegiscontrolplane_default` network
- **Host URL:** `http://localhost:3000` (host) / `http://aegis-juice:3000` (from Kali)

## Official Purpose
OWASP Juice Shop — modern intentionally vulnerable Node.js/Angular web app for XSS, SQLi, JWT, API abuse training.

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
curl -sI http://aegis-juice:3000
whatweb -a 3 http://aegis-juice:3000
```

## Full Output Summary
```
HTTP/1.1 200 OK
X-Recruiting: /#/jobs
Content-Type: text/html; charset=UTF-8

whatweb: [200 OK] HTML5, Title[OWASP Juice Shop], Script[module],
  UncommonHeaders[access-control-allow-origin,x-content-type-options,feature-policy,x-recruiting]
```

## What I Learned / Edge Cases / Gotchas
- Juice Shop was **not** in original Aegis compose — spun up by GrokStrike: `docker run -d --name aegis-juice --network aegiscontrolplane_default -p 3000:3000 bkimminich/juice-shop`
- SPA architecture: many paths are client-side routes (`/#/...`) — directory brute tools find less than on DVWA
- `X-Recruiting` header is an intentional CTF hint
- CORS `Access-Control-Allow-Origin: *` — API testing goldmine

## Effectiveness on This Target (1-10)
**10/10** — Ideal second target for modern web vuln practice

## Recommended Safe Parameters for Learning Labs
- Use `http://aegis-juice:3000` from Kali, `http://localhost:3000` from host browser
- Prefer API-focused tools: `nuclei`, `nikto`, `sqlmap` on REST endpoints, JWT tools
- Do not run aggressive brute force without rate limits

---
*GrokStrike v1.0 — 2026-06-24*