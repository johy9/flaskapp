#!/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "I am almost a Devops Engineer!"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('Starting Flask app...')
    app.run(host='0.0.0.0')
    logging.info('Flask app has been started')