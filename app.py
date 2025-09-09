import os
import requests
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB Setup
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.cti_dashboard
searches = db.searches

# API Keys
VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# VirusTotal API Query
def query_virustotal(ip_or_domain):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_or_domain}"
    headers = {"x-apikey": VT_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# AbuseIPDB API Query
def query_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {'Accept': 'application/json', 'Key': ABUSEIPDB_API_KEY}
    params = {'ipAddress': ip, 'maxAgeInDays': 90}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        query = request.form.get("query").strip()
        if query:
            vt_data = query_virustotal(query)
            abuse_data = query_abuseipdb(query)
            result = {
                "query": query,
                "virustotal": vt_data,
                "abuseipdb": abuse_data
            }
            # Save to DB
            searches.insert_one({
                "query": query,
                "virustotal": vt_data,
                "abuseipdb": abuse_data
            })
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
