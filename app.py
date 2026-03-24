import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello():
    app.logger.info("Root endpoint was hit")
    return "Hello DevOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)