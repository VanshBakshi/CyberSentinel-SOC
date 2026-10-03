# Architecture

```text
Security sources
      ↓
Event ingestion (JSON / CSV / API)
      ↓
Normalization + IOC extraction
      ↓
Rule engine ───────→ MITRE technique mapping
      ↓
Isolation Forest / PyTorch anomaly models
      ↓
Threat + anomaly + behavior risk scoring
      ↓
Correlation by entity + 20-minute windows
      ↓
Incident prioritization + timeline
      ↓
SOC dashboard / REST API / Elasticsearch
```

SQLite is the default persistence layer for easy local development. Elasticsearch is optional for search-oriented deployments.
