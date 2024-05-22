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


@app.route('/number/<int:n>', strict_slashes=False)
def number_display(n):
    """display “n is a number” only"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>',  strict_slashes=False)
def num_html(n):
    """Returns number in HTM L house"""
    return render_template('5-number.html', name=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_even_odd():
    """Dispaly the even or odd no."""
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run()
