# Cyber Threat Intelligence Dashboard

## Overview
A real-time threat intelligence dashboard built with Flask. It aggregates data from VirusTotal and AbuseIPDB APIs to provide reputation scores, threat metrics, and historical data on IPs/domains.

## Features
- Query IP/domain for threat info
- Displays VirusTotal & AbuseIPDB reputation and stats
- Stores queries & results in MongoDB
- User-friendly interface with Bootstrap
- Extendable for tagging and data export

## Setup
1. Clone repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add `.env` file with your API keys and MongoDB URI
4. Run: `flask run`

## Usage
Enter an IP or domain to get aggregated threat intelligence data.

---

## API Limits
Free tiers have rate limits — cache results when possible.

---

## License
MIT
