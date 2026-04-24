from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('request_count_total', 'Total request ke model')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Latency request')

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

@app.route('/predict')
def predict():
    with REQUEST_LATENCY.time():
        REQUEST_COUNT.inc()
    return {"message": "ok"}

if __name__ == '__main__':
    app.run(port=8000)