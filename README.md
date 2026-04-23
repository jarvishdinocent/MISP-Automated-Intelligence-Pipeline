# 🔐 MISP Automated Intelligence Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/MISP-Integration-green?style=for-the-badge&logo=misp" alt="MISP">
  <img src="https://img.shields.io/badge/Security-OSINT-red?style=for-the-badge" alt="Security OSINT">
</p>

---

## 📌 Overview

**MISP Automated Intelligence Pipeline** is a lightweight, Python-based threat intelligence ingestion engine. It is designed to **collect, deduplicate, score, and push** high-fidelity external threat feeds directly into your MISP instance.

> [!IMPORTANT]
> This tool transforms heterogeneous data (JSON, RSS) into structured MISP events with contextual tagging and automated scoring.

---

## 🎯 Key Objectives

* 🤖 **Automate** ingestion from world-class threat sources.
* 🧹 **Cleanse** data through MD5-based deduplication.
* 🧠 **Prioritize** intelligence with keyword-based scoring.
* 🏷️ **Contextualize** with automated TLP and Source tagging.

---

## ⚙️ Features

### 🔗 Integrated Threat Sources
| Source | Format | Type |
| :--- | :--- | :--- |
| **CISA KEV** | `JSON` | Exploited Vulnerabilities |
| **CISA ICS** | `RSS` | Industrial Control Systems |
| **NCSC UK** | `RSS` | National Advisories |
| **ANSSI** | `RSS` | French CERT Alerts |
| **BSI** | `RSS` | German CERT Alerts |

### 🧠 Intelligence Scoring Logic
The script analyzes titles and descriptions to assign a priority score:
* 🔴 **Critical** → `+50`
* 🟠 **Ransomware** → `+30`
* 🟡 **Exploit** → `+20`

---

## 🏗️ Workflow

External Feeds → Processing → Deduplication → Scoring → MISP Event Creation

## 📂 Project Structure

    ├── unified_feeds.py # Main logic & feed handlers
    ├── requirements.txt # Dependencies
    ├── .env             # Private configuration
    └── .gitignore       # Prevents credential leaks
    ├── LICENSE            # Project usage rights
    ├── README.md          # Documentation

## 🚀 Getting Started

1️⃣ Installation

# Clone the repository
* git clone https://github.com/jarvishdinocent/MISP-Automated-Intelligence-Pipeline.git
* cd MISP-Automated-Intelligence-Pipeline

# Setup virtual environment
* python3 -m venv venv
* source venv/bin/activate

# Install requirements
* pip install -r requirements.txt

2️⃣ Configuration

* Create a .env file in the root directory:
* MISP_URL="https://your-misp-instance"
* MISP_KEY="your-api-key"
* VERIFY_SSL=False

3️⃣ Execution

* python3 unified_feeds.py

## 📈 Output

The script will:

* Create MISP events per feed
* Populate attributes:
* CVE IDs (KEV)
* Advisory links (RSS feeds)
* Apply intelligence scores in comments
* Attach contextual tags
* Prevent duplicate entries

## ⚠️ Known Limitations

* Deduplication is per execution, not persistent
* Scoring is keyword-based (basic)
* Some feeds may return HTTP errors (e.g., 403/timeout)
* No MITRE ATT&CK mapping (yet)

## 🔐 Security Considerations
* Do NOT expose API keys publicly
* Use environment variables for production
* Disable SSL verification only in trusted environments

## 🚀 Future Improvements

* Persistent deduplication (database/file-based)
* Advanced scoring model
* Proxy support for restricted feeds
* MITRE ATT&CK enrichment
* Logging to file
