# CyberSentinel SOC

Enterprise-style Security Operations Center (SOC) intelligence platform for alert correlation, anomaly detection, incident prioritization, IOC extraction, and analyst workflow.

## What it does

Security events → normalization → rule detections → ML anomaly scoring → risk scoring → correlation → incident grouping → prioritized SOC dashboard.

### Included
- FastAPI REST API + Swagger docs
- Professional SOC dashboard
- JSON/CSV/bulk event ingestion
- Detection rules with MITRE ATT&CK technique tags
- Isolation Forest anomaly detection
- Optional PyTorch autoencoder training
- Alert deduplication and incident correlation
- Entity risk scoring
- IOC extraction for IPs, domains, and hashes
- Incident lifecycle: new / investigating / contained / resolved / false_positive
- Analyst notes
- Search and filtering
- Elasticsearch integration with SQLite fallback
- Demo data generator
- Health and metrics endpoints
- Docker Compose for Elasticsearch
- Tests and architecture/API documentation

## Quick start on Windows

### 1. Open this folder in VS Code

### 2. Run PowerShell starter
```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\start.ps1
```

The starter creates `.venv`, installs dependencies, seeds demo data, and starts the API.

### 3. Open
- Dashboard: http://127.0.0.1:8000
- Swagger API: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/api/health

### Manual start
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts\seed_demo.py
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

## Elasticsearch

The application works without Elasticsearch using SQLite. To enable Elasticsearch:
```powershell
docker compose up -d
```
Then set `ELASTICSEARCH_ENABLED=true` in `.env`.

## API examples

### Ingest event
```json
POST /api/events
{
  "event_type": "authentication",
  "severity": "high",
  "message": "Failed login burst detected",
  "src_ip": "10.10.10.44",
  "username": "admin",
  "failed_logins": 9,
  "bytes_in": 1200,
  "bytes_out": 500
}
```

### Train anomaly model
`POST /api/ml/train`

### Rebuild incidents
`POST /api/incidents/rebuild`

## Project structure

```text
CyberSentinel-SOC/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── services/
│   ├── main.py
│   └── schemas.py
├── frontend/
├── scripts/
├── tests/
├── docs/
├── data/
├── models/
├── docker-compose.yml
├── requirements.txt
├── start.ps1
└── start.bat
```

## Defensive use

This project is designed for authorized defensive monitoring, detection, triage, and incident response workflows.
