#!/usr/bin/python3
"""Flask framework for hello world"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """return Hello"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
