# Aegis MCP Bridge API

```json
{
  "name": "aegis-mcp-bridge",
  "category": "api",
  "endpoints": {
    "GET /health": "Returns status, tool count, Ollama host",
    "POST /": "JSON-RPC: tools/list, tools/call, ollama/chat, health"
  },
  "port": 8899,
  "note": "HexStrike-inspired offline MCP bridge in aegis-controlplane"
}
```
