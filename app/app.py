import os
from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total HTTP Requests')

VERSION = os.environ.get("APP_VERSION", "unknown")
COLOR = os.environ.get("APP_COLOR", "unknown")

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return f"Hello namaste bhai! GitOps app is Running! Version: {VERSION} | Color: {COLOR}"

@app.route('/health')
def health():
    return {"status": "healthy", "version": VERSION, "color": COLOR}, 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)