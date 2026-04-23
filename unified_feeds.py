#!/usr/bin/env python3

import requests
import feedparser
import urllib3
import hashlib
from datetime import datetime
from pymisp import PyMISP, MISPEvent

urllib3.disable_warnings()

# ================= CONFIG =================
MISP_URL = "YOUR_ACTUAL_MISP_URL"
MISP_KEY = "YOUR_API_KEY"
VERIFY_SSL = False

misp = PyMISP(MISP_URL, MISP_KEY, ssl=VERIFY_SSL)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# ================= UTIL =================

def log(msg):
    print(f"[{datetime.now()}] {msg}")

def generate_hash(value):
    return hashlib.md5(value.encode()).hexdigest()

def score_intel(text):
    score = 0
    text = text.lower()
    if "critical" in text: score += 50
    if "ransomware" in text: score += 30
    if "exploit" in text: score += 20
    return score

def safe_request(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20, verify=False)
        if r.status_code != 200:
            log(f"[ERROR] {url} returned {r.status_code}")
            return None
        return r
    except Exception as e:
        log(f"[ERROR] {url} failed → {e}")
        return None

def create_event_with_data(title, attributes, source_tag):
    if not attributes:
        log(f"[SKIPPED] No valid data for {title}")
        return

    event = MISPEvent()
    event.info = title
    event.distribution = 3   # TLP WHITE requires this
    event.threat_level_id = 2
    event.analysis = 0

    event = misp.add_event(event, pythonify=True)

    # add attributes
    for attr in attributes:
        event.add_attribute("link", attr["value"], comment=attr["comment"])

    misp.update_event(event)

    # tagging (safe)
    for tag in ["osint", f"source:{source_tag}", "tlp:white"]:
        try:
            misp.tag(event.uuid, tag)
        except:
            log(f"[TAG FAIL] {tag}")

    log(f"[+] Event {event.id} created with {len(attributes)} attributes")

# ================= FEEDS =================

def fetch_cisa_kev():
    log("[*] CISA KEV")

    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    r = safe_request(url)
    if not r:
        return

    try:
        data = r.json()
    except:
        log("[ERROR] KEV JSON failed")
        return

    seen = set()
    attributes = []

    for vuln in data.get("vulnerabilities", []):
        cve = vuln.get("cveID")
        if not cve:
            continue

        h = generate_hash(cve)
        if h in seen:
            continue
        seen.add(h)

        score = score_intel(vuln.get("shortDescription", ""))

        attributes.append({
            "value": cve,
            "comment": f"KEV | Score: {score}"
        })

    create_event_with_data("CISA KEV", attributes, "cisa")

def fetch_rss(name, url, source_tag):
    log(f"[*] {name}")

    feed = feedparser.parse(url)

    if not feed.entries:
        log(f"[SKIPPED] No entries in {name}")
        return

    seen = set()
    attributes = []

    for entry in feed.entries:
        link = entry.get("link")
        title = entry.get("title", "")

        if not link:
            continue

        h = generate_hash(link)
        if h in seen:
            continue
        seen.add(h)

        score = score_intel(title)

        attributes.append({
            "value": link,
            "comment": f"{title} | Score: {score}"
        })

    create_event_with_data(name, attributes, source_tag)

# ================= MAIN =================

def main():
    log("===== START =====")

    fetch_cisa_kev()

    fetch_rss("CISA ICS",
              "https://www.cisa.gov/uscert/ics/advisories.xml",
              "cisa-ics")

    fetch_rss("NCSC UK",
              "https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml",
              "ncsc-uk")

    fetch_rss("ANSSI",
              "https://www.cert.ssi.gouv.fr/feed/",
              "anssi")

    fetch_rss("BSI",
              "https://www.bsi.bund.de/SiteGlobals/Functions/RSSFeed/RSSNewsfeed.xml",
              "bsi")

    log("===== END =====")

if __name__ == "__main__":
    main()
