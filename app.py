from flask import Flask, render_template, request
from datetime import datetime
import requests
import os

app = Flask(__name__)
visitor_log = []

def get_geolocation(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return f"{data.get('city', 'Unknown')}, {data.get('country', 'Unknown')}"
    except:
        return "Unknown"

@app.route("/")
def index():
    ip = request.remote_addr
    visitor_info = {
        "ip": ip,
        "message": request.args.get("msg", "None"),
        "username": request.args.get("user", "Anonymous"),
        "geo": get_geolocation(ip),
        "user_agent": request.headers.get("User-Agent"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "referrer": request.referrer or "Direct",
        "language": request.headers.get("Accept-Language", "Unknown"),
        "method": request.method,
        "path": request.path
    }
    visitor_log.append(visitor_info)
    return render_template("index.html", visitors=visitor_log)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
