from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)
visitor_log = []

@app.route("/")
def index():
    visitor_info = {
        "ip": request.remote_addr,
        "user_agent": request.headers.get('User-Agent'),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    visitor_log.append(visitor_info)
    return render_template("index.html", visitors=visitor_log)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
