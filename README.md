# 🔐 MISP Automated Intelligence Pipeline

## 📌 Overview

**MISP Automated Intelligence Pipeline** is a lightweight, Python-based threat intelligence ingestion script designed to **collect, deduplicate, score, and push external threat feeds into MISP**.

The script integrates multiple public threat intelligence sources and transforms them into structured MISP events with contextual tagging and scoring.

---

## 🎯 Objective

* Automate ingestion of external threat intelligence feeds
* Normalize and process heterogeneous data formats (JSON, RSS)
* Remove duplicate indicators
* Assign basic intelligence scoring
* Populate MISP with structured and tagged events

---

## ⚙️ Features

### 🔗 Threat Intelligence Sources

Currently integrated feeds:

* **CISA Known Exploited Vulnerabilities (KEV)** (JSON)
* **CISA ICS Advisories** (RSS)
* **NCSC UK Advisories** (RSS)
* **ANSSI (CERT-FR)** (RSS)
* **BSI (Germany CERT)** (RSS)

---

### 🧹 Data Processing

* JSON and RSS parsing
* Data normalization
* Error-handled HTTP requests
* Resilient ingestion pipeline

---

### 🔁 Deduplication

* MD5 hash-based deduplication
* Prevents duplicate indicators within each feed
* Ensures cleaner MISP events

---

### 🧠 Intelligence Scoring

Basic keyword-based scoring:

* `critical` → +50
* `ransomware` → +30
* `exploit` → +20

Used to prioritize indicators inside MISP attributes.

---

### 🏷️ Automated Tagging

Each event is tagged with:

* `osint`
* `source:<feed-name>`
* `tlp:white`

---

### 📊 MISP Integration

* Automatic event creation
* Attribute population (`link`, `CVE`)
* Event tagging
* Distribution aligned with TLP

---

## 🏗️ Workflow

```id="flow1"
External Feeds → Processing → Deduplication → Scoring → MISP Event Creation
```

---

## 🖥️ Environment

| Component | Value                  |
| --------- | ---------------------- |
| MISP URL  | https://192.168.210.38 |
| Script    | unified_feeds.py       |

---

## 📂 Project Structure

```id="struct1"
.
├── unified_feeds.py
├── requirements.txt
├── config.example.py
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash id="clone1"
git clone https://github.com/your-username/MISP-Automated-Intelligence-Pipeline.git
cd MISP-Automated-Intelligence-Pipeline
```

---

### 2️⃣ Setup Environment

```bash id="env1"
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash id="dep1"
pip install -r requirements.txt
```

---

## 🔧 Configuration

Edit the script or use config file:

```python id="config1"
MISP_URL = "https://192.168.210.38"
MISP_KEY = "YOUR_API_KEY"
VERIFY_SSL = False
```

---

## ▶️ Execution

```bash id="run1"
python3 unified_feeds.py
```

---

## 📈 Output

The script will:

* Create MISP events per feed
* Populate attributes:

  * CVE IDs (KEV)
  * Advisory links (RSS feeds)
* Apply intelligence scores in comments
* Attach contextual tags
* Prevent duplicate entries

---

## ⚠️ Known Limitations

* Deduplication is **per execution**, not persistent
* Scoring is keyword-based (basic)
* Some feeds may return HTTP errors (e.g., 403/timeout)
* No MITRE ATT&CK mapping (yet)

---

## 🔐 Security Considerations

* Do NOT expose API keys publicly
* Use environment variables for production
* Disable SSL verification only in trusted environments

---

## 🚀 Future Improvements

* Persistent deduplication (database/file-based)
* Advanced scoring model
* Proxy support for restricted feeds
* MITRE ATT&CK enrichment
* Logging to file


