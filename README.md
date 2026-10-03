# 🤖⚡ CyberSentinel SOC

### Autonomous AI-Powered Security Operations & Threat Intelligence Platform

<p align="center">

```text
   ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     
  ██║       ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     
  ╚██████╗   ██║   ██║     ███████╗██║  ██║███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗
   ╚═════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
```

### 🛡️ AI SECURITY ROBOT ONLINE

**Observe → Detect → Correlate → Analyze → Prioritize → Investigate → Respond**

</p>

---

# 🧠 What is CyberSentinel SOC?

**CyberSentinel SOC** is an AI-powered Security Operations Center platform designed to help security teams process huge volumes of security alerts and identify the events that actually require investigation.

Modern organizations generate thousands or millions of security events every day:

```text
Servers
   │
   ├── Authentication Logs
   ├── Network Events
   ├── Endpoint Events
   ├── Application Logs
   ├── Firewall Alerts
   ├── Cloud Events
   └── Security Tools
          │
          ▼
   ┌───────────────────────┐
   │   CYBERSENTINEL SOC   │
   │     🤖 AI ROBOT       │
   └───────────────────────┘
          │
          ▼
   Detect → Correlate → Score
          │
          ▼
   Human Analysts
```

Instead of forcing analysts to manually investigate every alert, CyberSentinel processes events automatically and produces **prioritized incidents with explainable risk factors**.

---

# 🎯 Real-World Problem

Security Operations Centers face several major problems:

* 🔴 Extremely high alert volumes
* 🟠 Duplicate security alerts
* 🟡 False positives
* 🔵 Isolated events that look harmless individually
* 🟣 Difficult incident prioritization
* ⚫ Lack of context between events
* 🟢 Limited analyst time
* 🔥 Increasingly sophisticated attacks

For example:

```text
Alert #001 → Failed Login
Alert #002 → Failed Login
Alert #003 → Failed Login
Alert #004 → PowerShell
Alert #005 → Credential Access
Alert #006 → Outbound Data Transfer
Alert #007 → Suspicious Network Activity
```

Individually:

```text
LOW RISK
```

Together:

```text
                    🚨 HIGH RISK INCIDENT 🚨

        ┌─────────────────────────────────────┐
        │       POSSIBLE ATTACK CHAIN         │
        ├─────────────────────────────────────┤
        │ Brute Force                         │
        │        ↓                            │
        │ Account Compromise                  │
        │        ↓                            │
        │ PowerShell Execution                │
        │        ↓                            │
        │ Credential Access                   │
        │        ↓                            │
        │ Suspicious Network Activity         │
        │        ↓                            │
        │ Possible Data Exfiltration          │
        └─────────────────────────────────────┘
```

CyberSentinel is designed to identify this relationship automatically.

---

# 🤖 CyberSentinel AI Robot

The core concept is an autonomous SOC intelligence engine.

```text
                         🤖
                    CYBERSENTINEL
                         │
              ┌──────────┴──────────┐
              │   SECURITY BRAIN    │
              └──────────┬──────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
     DETECT           ANALYZE          CORRELATE
        │                │                │
        ▼                ▼                ▼
      Rules             ML             Events
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                  RISK INTELLIGENCE
                         │
                         ▼
                 INCIDENT PRIORITY
                         │
                         ▼
                  👨‍💻 SOC ANALYST
```

The robot does not replace the security analyst.

It acts as an **AI assistant that reduces repetitive analysis and brings important incidents to human attention faster.**

---

# 🚀 Core Capabilities

## 🛡️ 1. Security Event Ingestion

CyberSentinel accepts security events from different sources.

```text
               SECURITY DATA
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
    Windows       Linux        Network
      Logs         Logs         Events
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
              EVENT INGESTION
```

Supported ingestion concepts include:

* JSON
* CSV
* API events
* Application logs
* Authentication events
* Network events
* Endpoint events

---

# 🧹 2. Event Normalization

Different security systems produce different formats.

CyberSentinel converts them into a common structure.

```text
Raw Event
    │
    ▼
┌─────────────────────────┐
│ Event Normalizer        │
├─────────────────────────┤
│ Timestamp               │
│ Source IP               │
│ Destination IP          │
│ Username                │
│ Hostname                │
│ Event Type              │
│ Message                 │
│ Bytes                   │
│ Severity                │
└────────────┬────────────┘
             │
             ▼
      Standard Event
```

This makes downstream analysis easier.

---

# 🔍 3. Rule-Based Threat Detection

The first detection layer uses security rules.

Example:

```text
Failed Login × 5
       │
       ▼
BRUTE FORCE DETECTED
       │
       ▼
MITRE: T1110
```

Other detection patterns include:

```text
PowerShell Activity
        ↓
Execution Detection

Credential Keywords
        ↓
Credential Access Detection

Port Scan
        ↓
Network Discovery Detection

Ransomware Indicators
        ↓
Impact Detection
```

---

# 🧠 4. Machine Learning Anomaly Detection

CyberSentinel also analyzes behavior instead of relying only on predefined rules.

### Isolation Forest

The system evaluates features such as:

```text
Bytes In
Bytes Out
Failed Logins
Threat Score
Message Length
External Connection
```

The ML engine attempts to identify unusual behavior.

```text
                 EVENTS
                    │
                    ▼
             Feature Extraction
                    │
                    ▼
             ML Model
                    │
          ┌─────────┴─────────┐
          │                   │
       NORMAL              ANOMALOUS
          │                   │
          ▼                   ▼
       Continue           Investigate
```

---

# 🧬 5. PyTorch AI Layer

CyberSentinel can also use a neural-network-based anomaly detection approach.

```text
Security Event
      │
      ▼
Feature Vector
      │
      ▼
┌─────────────────────┐
│   Neural Network    │
│      Encoder        │
└──────────┬──────────┘
           │
           ▼
      Latent Space
           │
           ▼
┌─────────────────────┐
│     Decoder         │
└──────────┬──────────┘
           │
           ▼
 Reconstruction Error
           │
           ▼
   Anomaly Indicator
```

This allows the platform to explore more advanced behavioral detection.

---

# 🔗 6. Alert Correlation Engine

This is one of the most important components.

Instead of treating every alert as an isolated event:

```text
Alert 1
Alert 2
Alert 3
Alert 4
Alert 5
```

CyberSentinel looks for relationships.

```text
             ┌──────────────┐
             │   Alert #1   │
             └──────┬───────┘
                    │
             Same Source IP
                    │
             ┌──────▼───────┐
             │   Alert #2   │
             └──────┬───────┘
                    │
             Same User
                    │
             ┌──────▼───────┐
             │   Alert #3   │
             └──────┬───────┘
                    │
             Same Host
                    │
             ┌──────▼───────┐
             │   Alert #4   │
             └──────┬───────┘
                    │
                    ▼
             INCIDENT CLUSTER
```

Correlation uses factors such as:

* Source IP
* Username
* Hostname
* Event type
* Time window
* Threat indicators
* Suspicious behavior

---

# ⚠️ 7. Risk Scoring Engine

Every security event receives a calculated risk score.

Example:

```text
                 EVENT
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
    Threat      Anomaly     Behavior
    Score        Score        Score
       │           │           │
       └───────────┼───────────┘
                   │
                   ▼
             RISK ENGINE
                   │
                   ▼
              SCORE: 87
                   │
                   ▼
               🔴 HIGH
```

Risk factors can include:

* Rule detections
* Failed login count
* Network behavior
* Outbound data volume
* ML anomaly score
* Event severity
* Suspicious keywords
* Number of related events

---

# 🚨 8. Incident Prioritization

Instead of showing analysts thousands of alerts, CyberSentinel organizes incidents by priority.

```text
┌─────────────────────────────────────────┐
│           SOC INCIDENT QUEUE            │
├─────────────────────────────────────────┤
│ 🔴 CRITICAL   Possible Ransomware       │
│ 🔴 CRITICAL   Credential Attack         │
│ 🟠 HIGH       Suspicious PowerShell     │
│ 🟠 HIGH       Network Scan              │
│ 🟡 MEDIUM     Failed Authentication     │
│ 🟢 LOW        Informational Event       │
└─────────────────────────────────────────┘
```

The score is designed to help analysts decide what deserves attention first.

---

# 🧩 9. MITRE ATT&CK Mapping

CyberSentinel can associate detections with MITRE-style tactics and techniques.

Example:

```text
Brute Force
     │
     └── T1110
          │
          └── Credential Access

PowerShell
     │
     └── T1059
          │
          └── Command & Scripting Interpreter

Port Scan
     │
     └── T1046
          │
          └── Network Service Scanning

Ransomware
     │
     └── T1486
          │
          └── Data Encrypted for Impact
```

This provides security analysts with additional context during investigation.

---

# 🕵️ 10. IOC Extraction

CyberSentinel can extract potential indicators from event messages.

```text
                    LOG MESSAGE
                         │
                         ▼
              ┌────────────────────┐
              │    IOC ENGINE       │
              └─────────┬──────────┘
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
        IPv4         Domain         Hash
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  IOC DATABASE
```

Potential indicators include:

* IPv4 addresses
* Domains
* File hashes

---

# 🧠 11. Explainable Risk Analysis

CyberSentinel doesn't only provide:

```text
Risk = 92
```

It can also show why.

Example:

```text
INCIDENT RISK ANALYSIS
────────────────────────────────────

Risk Score: 92

Factors:

✓ Multiple failed logins
✓ PowerShell execution
✓ Credential-related activity
✓ External network connection
✓ ML anomaly detected
✓ Multiple correlated events

Priority:
CRITICAL
```

This helps analysts understand the reasoning behind prioritization.

---

# 🔎 12. Security Search

Analysts can search across security events and incidents.

Example:

```text
Search:
185.199.88.42
```

Possible results:

```text
185.199.88.42
      │
      ├── Authentication Events
      ├── Network Events
      ├── Suspicious Commands
      ├── Related Users
      └── Related Incidents
```

---

# 🗂️ 13. Incident Lifecycle

CyberSentinel supports an analyst workflow.

```text
                NEW
                 │
                 ▼
           INVESTIGATING
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
     FALSE             CONTAINED
    POSITIVE               │
                            ▼
                         RESOLVED
```

This allows incidents to move through a basic SOC workflow.

---

# 📊 14. SOC Dashboard

The dashboard provides a central security overview.

```text
╔════════════════════════════════════════════════════════════╗
║ 🤖 CYBERSENTINEL SOC                         ● AI ONLINE  ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  EVENTS        INCIDENTS       CRITICAL       ANOMALIES    ║
║  15,842           127              12             84       ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║             THREAT INTELLIGENCE CORE                       ║
║                                                            ║
║   🔴 Critical       ███████████████                        ║
║   🟠 High           ███████████                            ║
║   🟡 Medium         ███████                                ║
║   🟢 Low            ████                                   ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                  LIVE SECURITY EVENTS                      ║
║                                                            ║
║  20:31:22  🔴 Brute Force      185.xxx.xxx.xxx             ║
║  20:31:25  🟠 PowerShell       SERVER-04                  ║
║  20:31:31  🔴 Credential       ADMIN                      ║
║  20:31:39  🟡 Network Scan     SERVER-07                  ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │   SECURITY SOURCES   │
                         ├──────────────────────┤
                         │ Windows / Linux      │
                         │ Network / Firewall   │
                         │ Applications         │
                         │ Endpoint Systems     │
                         │ Cloud Events         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   EVENT INGESTION    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    NORMALIZATION     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                ┌───────────────────┴───────────────────┐
                │                                       │
                ▼                                       ▼
       ┌──────────────────┐                    ┌──────────────────┐
       │ RULE DETECTION   │                    │ ML ANOMALY       │
       │                  │                    │ DETECTION         │
       └────────┬─────────┘                    └────────┬─────────┘
                │                                       │
                └───────────────────┬───────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ CORRELATION ENGINE   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   RISK SCORING      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ INCIDENT ENGINE      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                     ┌────────────────────────────┐
                     │     SOC DASHBOARD          │
                     │                            │
                     │  🤖 AI SECURITY ANALYST    │
                     └─────────────┬──────────────┘
                                   │
                                   ▼
                         👨‍💻 HUMAN SECURITY TEAM
```

---

# 🔄 Complete Detection Pipeline

```text
                    SECURITY EVENT
                          │
                          ▼
                  ┌───────────────┐
                  │    INGEST     │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   NORMALIZE   │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ RULE ENGINE   │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ FEATURE ENGINE │
                  └───────┬───────┘
                          │
                          ▼
              ┌───────────────────────┐
              │      AI / ML          │
              │ Isolation Forest      │
              │ PyTorch Autoencoder   │
              └───────────┬───────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │  CORRELATION  │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ RISK ENGINE   │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ INCIDENT      │
                  │ CREATION      │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ SOC DASHBOARD │
                  └───────┬───────┘
                          │
                          ▼
                    👨‍💻 ANALYST
```

---

# 🧰 Technology Stack

| Layer                 | Technology                |
| --------------------- | ------------------------- |
| Backend               | Python                    |
| API                   | FastAPI                   |
| API Server            | Uvicorn                   |
| Database              | SQLite                    |
| Search / SIEM Storage | Elasticsearch             |
| Data Processing       | Pandas                    |
| Numerical Computing   | NumPy                     |
| Machine Learning      | Scikit-learn              |
| Anomaly Detection     | Isolation Forest          |
| Deep Learning         | PyTorch                   |
| ORM                   | SQLAlchemy                |
| Validation            | Pydantic                  |
| Frontend              | HTML5 / CSS3 / JavaScript |
| Containerization      | Docker                    |
| Testing               | Pytest                    |
| Configuration         | `.env`                    |
| Logging               | Python Logging            |

---

# 📁 Project Architecture

```text
CyberSentinel-SOC/
│
├── 🤖 app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   └── services/
│       ├── detection.py
│       ├── scoring.py
│       ├── ml_engine.py
│       ├── torch_model.py
│       ├── correlation.py
│       └── elasticsearch_store.py
│
├── 🖥️ frontend/
│   ├── index.html
│   └── static/
│       ├── style.css
│       └── app.js
│
├── 🧪 tests/
│   └── test_scoring.py
│
├── 📊 scripts/
│   └── seed_demo.py
│
├── 📚 docs/
│   ├── ARCHITECTURE.md
│   └── API_EXAMPLES.md
│
├── 🧠 models/
├── 📦 data/
│
├── requirements.txt
├── docker-compose.yml
├── .env.example
├── .gitignore
├── start.ps1
├── start.bat
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/VanshBakshi/CyberSentinel-SOC.git
cd CyberSentinel-SOC
```

---

## 2️⃣ Create Virtual Environment

### Windows

```powershell
py -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3️⃣ Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

# ▶️ Run CyberSentinel SOC

The easiest way:

```powershell
.\start.ps1
```

Or:

```powershell
.\start.bat
```

Manual startup:

```powershell
python scripts/seed_demo.py
python -m uvicorn app.main:app --reload
```

---

# 🌐 Access the SOC

### Dashboard

```text
http://127.0.0.1:8000
```

### API Documentation

```text
http://127.0.0.1:8000/docs
```

### Health Check

```text
http://127.0.0.1:8000/api/health
```

---

# 🐳 Docker

Start Elasticsearch:

```bash
docker compose up -d
```

Check:

```text
http://localhost:9200
```

CyberSentinel can operate with SQLite while Elasticsearch is unavailable, making the project easier to run locally.

---

# 🔌 API Overview

| Endpoint                 | Method | Purpose              |
| ------------------------ | ------ | -------------------- |
| `/api/health`            | GET    | System health        |
| `/api/stats`             | GET    | SOC statistics       |
| `/api/events`            | GET    | Security events      |
| `/api/events`            | POST   | Create event         |
| `/api/events/bulk`       | POST   | Bulk ingestion       |
| `/api/events/upload`     | POST   | Upload events        |
| `/api/events/{id}`       | GET    | Event details        |
| `/api/ml/train`          | POST   | Train anomaly model  |
| `/api/incidents`         | GET    | Incident list        |
| `/api/incidents/rebuild` | POST   | Rebuild incidents    |
| `/api/incidents/{id}`    | GET    | Incident details     |
| `/api/incidents/{id}`    | PATCH  | Update incident      |
| `/api/search`            | GET    | Search security data |

---

# 🧪 Demo Security Scenario

CyberSentinel includes demo data that simulates realistic SOC activity.

Example attack sequence:

```text
                    INTERNET
                       │
                       ▼
              ┌────────────────┐
              │ Suspicious IP  │
              └───────┬────────┘
                      │
                      ▼
              Failed Login × 8
                      │
                      ▼
                Brute Force
                      │
                      ▼
              Account Activity
                      │
                      ▼
              PowerShell Event
                      │
                      ▼
             Credential Activity
                      │
                      ▼
             Network Connection
                      │
                      ▼
             Large Data Transfer
                      │
                      ▼
                 🚨 INCIDENT
                      │
                      ▼
                🤖 AI ANALYSIS
                      │
                      ▼
              HIGH / CRITICAL RISK
```

---

# 🧠 AI Decision Architecture

CyberSentinel combines multiple intelligence layers.

```text
                 ┌────────────────────┐
                 │   SECURITY EVENT   │
                 └─────────┬──────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
       Rule Engine      ML Engine      IOC Engine
            │              │              │
            │              │              │
            └──────────────┼──────────────┘
                           │
                           ▼
                  Correlation Engine
                           │
                           ▼
                    Risk Calculator
                           │
                           ▼
                  Incident Generator
                           │
                           ▼
                     SOC Analyst
```

This layered architecture reduces dependence on a single detection method.

---

# 🔐 Security Design Principles

CyberSentinel follows several defensive security principles:

```text
Least Privilege
      │
      ▼
Defense in Depth
      │
      ▼
Continuous Monitoring
      │
      ▼
Explainable Detection
      │
      ▼
Human-in-the-Loop
      │
      ▼
Auditable Investigation
```

The platform is designed for **defensive security analysis and incident investigation**.

---

# 📈 Future Enterprise Extensions

The architecture can be extended with:

```text
                    CYBERSENTINEL
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   Threat Intel       SOAR Actions      LLM Analyst
        │                 │                 │
        ▼                 ▼                 ▼
   IOC Enrichment     Automation       Investigation
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
                  Enterprise SOC
```

Potential future integrations:

* SIEM connectors
* Threat intelligence APIs
* Cloud security logs
* EDR data
* Windows Event Logs
* Linux audit logs
* Firewall logs
* LLM-based investigation assistant
* Automated report generation
* SOAR workflows
* Role-based access control
* PostgreSQL
* Redis
* Kafka
* Kubernetes
* Prometheus/Grafana
* Enterprise authentication

---

# 🧪 Testing

Run:

```powershell
pytest
```

The test suite validates important components such as risk scoring.

---

# 📊 Example Security Event

```json
{
  "event_type": "authentication",
  "src_ip": "185.199.88.42",
  "username": "admin",
  "hostname": "SERVER-01",
  "failed_logins": 8,
  "message": "Multiple failed login attempts detected",
  "severity": "high"
}
```

CyberSentinel processes this through:

```text
INPUT
  ↓
NORMALIZATION
  ↓
RULE DETECTION
  ↓
FEATURE EXTRACTION
  ↓
ML ANALYSIS
  ↓
CORRELATION
  ↓
RISK SCORING
  ↓
INCIDENT
  ↓
SOC DASHBOARD
```

---

# 🤖 CyberSentinel Philosophy

```text
       ┌───────────────────────────────┐
       │        SECURITY DATA          │
       └───────────────┬───────────────┘
                       │
                       ▼
                  🤖 SENTINEL
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       OBSERVE       THINK        DETECT
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                    CORRELATE
                       │
                       ▼
                     SCORE
                       │
                       ▼
                  PRIORITIZE
                       │
                       ▼
                👨‍💻 HUMAN ANALYST
```

### The goal is simple:

> **Don't make security teams search through every alert.
> Help them focus their attention where the evidence indicates investigation is warranted.**

---

# 👨‍💻 Developer

**Vansh Bakshi**

BCA | Full Stack Developer | Python Developer | AI/ML | Cybersecurity

### Areas

```text
Python
AI / ML
Cybersecurity
FastAPI
Flutter
Full Stack Development
Data Analysis
Generative AI
```

---

# ⭐ Project Vision

CyberSentinel SOC is built as a portfolio-grade implementation of a modern **AI-assisted Security Operations Center**.

The long-term vision is:

```text
                 ┌──────────────────────┐
                 │   SECURITY WORLD     │
                 └──────────┬───────────┘
                            │
                            ▼
                     🤖 CYBERSENTINEL
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
           DETECT        ANALYZE       CORRELATE
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ▼
                       PRIORITIZE
                            │
                            ▼
                     🛡️ PROTECT
                            │
                            ▼
                    👨‍💻 HUMAN SOC
```

**CyberSentinel SOC — turning security noise into actionable intelligence.** 🛡️🤖⚡

---

## 📜 License

This project is intended for educational, research, portfolio, and defensive cybersecurity use.
