🔐 MISP Automated Intelligence Pipeline
📌 Overview
MISP Automated Intelligence Pipeline is a lightweight, Python-based threat intelligence ingestion script designed to collect, deduplicate, score, and push external threat feeds into MISP.

The script integrates multiple public threat intelligence sources and transforms them into structured MISP events with contextual tagging and scoring.

🎯 Objective
Automate ingestion of external threat intelligence feeds

Normalize and process heterogeneous data formats (JSON, RSS)

Remove duplicate indicators

Assign basic intelligence scoring

Populate MISP with structured and tagged events

⚙️ Features
🔗 Threat Intelligence Sources
CISA Known Exploited Vulnerabilities (KEV) (JSON)

CISA ICS Advisories (RSS)

NCSC UK Advisories (RSS)

ANSSI (CERT-FR) (RSS)

BSI (Germany CERT) (RSS)

🧠 Intelligence Scoring
Basic keyword-based scoring applied to event comments:

critical → +50

ransomware → +30

exploit → +20

🏷️ Automated Tagging
Each event is automatically tagged for easy filtering:

osint

source:<feed-name>

tlp:white

🏗️ Workflow
Plaintext
External Feeds (JSON/RSS) → Parsing → Deduplication → Scoring → MISP API → Event Created
📂 Project Structure
Plaintext
.
├── unified_feeds.py   # Main execution script
├── requirements.txt   # Python dependencies
├── .env               # Private configuration (ignored by git)
├── .gitignore         # Git exclusion rules
├── LICENSE            # Project license
└── README.md          # Documentation
⚙️ Installation
1️⃣ Clone Repository
Bash
git clone https://github.com/your-username/MISP-Automated-Intelligence-Pipeline.git
cd MISP-Automated-Intelligence-Pipeline
2️⃣ Setup Environment
Bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
Bash
pip install -r requirements.txt
🔧 Configuration
The script uses a .env file to manage sensitive credentials. Create a file named .env in the root directory:

Ini, TOML
MISP_URL=https://your-misp-instance.com
MISP_KEY=your_api_key_here
VERIFY_SSL=False
Note: Ensure .env is listed in your .gitignore to prevent leaking your API keys.

▶️ Execution
Simply run the unified script to start the ingestion process:

Bash
python3 unified_feeds.py
📈 Output
The script will:

Create unique MISP events per source.

Automatically assign attribute types (vulnerability for CVEs, link for advisories).

Apply intelligence scores in the attribute comments.

Prevent duplicate entries within the same execution session.

🔐 Security Considerations
API Safety: Never commit your .env file to version control.

SSL Verification: Setting VERIFY_SSL=False is common for local/lab MISP instances but should be handled with caution in production environments.

Permissions: Ensure the MISP API key used has "Add Event" permissions.

🚀 Future Improvements
Persistent deduplication using a local SQLite database.

MITRE ATT&CK mapping enrichment.

Advanced scoring based on CVSS scores.

Automated scheduling via Cron or Docker.
