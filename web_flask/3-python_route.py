#!/usr/bin/python3
"""Flask framework for hello world"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """return Hello"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB 2nd page"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def text_display(text):
    """return any string"""
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """display “Python ”, adn anyother thing"""
    return "Python".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
