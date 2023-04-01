#!/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello there! I am almost a DevOps Engineer in the making, and I am excited to use Flask to build some awesome web applications. Stay tuned for some amazing projects coming soon!"

if __name__ == "__main__":
 app.run(host='0.0.0.0')
