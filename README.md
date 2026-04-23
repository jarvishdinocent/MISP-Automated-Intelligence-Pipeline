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
.
├── unified_feeds.py   # Main logic & feed handlers
├── requirements.txt   # Dependencies
├── .env               # Private configuration (DO NOT COMMIT)
├── .gitignore         # Prevents credential leaks
├── LICENSE            # Project usage rights
└── README.md          # Documentation

## 🚀 Getting Started

1️⃣ Installation

# Clone the repository
git clone [https://github.com/your-username/MISP-Automated-Intelligence-Pipeline.git](https://github.com/your-username/MISP-Automated-Intelligence-Pipeline.git)
cd MISP-Automated-Intelligence-Pipeline

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

2️⃣ Configuration

Create a .env file in the root directory:
MISP_URL="https://your-misp-instance"
MISP_KEY="your-api-key"
VERIFY_SSL=False

3️⃣ Execution
python3 unified_feeds.py

## 📈 Output Examples
When executed, the script creates structured events in MISP:

Attributes: Automatically detects vulnerability (CVE) vs link.

Comments: Includes the specific feed source and calculated score.

Tags: Applied osint, tlp:white, and source:<name>.
