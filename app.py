from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus counter
REQUEST_COUNT = Counter("app_requests_total", "Total HTTP requests")

@app.before_request
def before_request():
    REQUEST_COUNT.inc() 

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)