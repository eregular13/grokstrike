# GrokStrike Environment — v2 Full Bootstrap

## SAFETY CHECK PASSED — local Docker lab only

| Container | Role | Endpoint |
|-----------|------|----------|
| aegis-kali | Attacker | docker exec aegis-kali |
| aegis-target | DVWA | http://localhost:8080 |
| aegis-juice | Juice Shop | http://localhost:3000 |
| aegis-controlplane | MCP :8899 | http://localhost:8899/health |

**Bootstrap:** `scripts/kali-full-bootstrap.sh` — SUCCESS
**Tools documented:** 184
**Generated:** 2026-06-24T05:48:54.929555+00:00
