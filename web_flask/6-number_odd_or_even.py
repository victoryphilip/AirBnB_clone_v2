#!/usr/bin/python3
#<<<<<<< HEAD
'''
    starts a Flask web app.
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello():
    '''
        Shows `Hello HBNB!`.
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
        Shows `HBNB`.
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    '''
        Displays 'C' followed by the value of <text>.
    '''
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    '''
        Displays 'Python' followed by the value of <text>.
    '''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''
        Displays 'n' followed by the value of <text>.
    '''
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    '''
        Displays an HTML page if 'n' is int.
    '''
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    '''
        Displays n if odd or even.
    '''
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
#=======
""" This is the 6th Flask setup script. """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Flask route at root.
        Displays 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Flask route at /hbnb.
        Displays 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
        Flask route at /c/<text>.
        Displays 'C + <text>'.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
        Flask route at /python/(<text>).
        Displays 'Python + <text>'.
        Default value of <text> : 'is cool'.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        Flask route at /number/<n>.
        Displays '<n> + is an number' if <n> is a int.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
        Flask route at /number_template/<n>.
        Displays the 5-number.html template wiht value of <n>.
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
        Flask route at /number_odd_or_even/<n>.
        Displays the 6-number_odd_or_even.html template wiht value of <n>.
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
#>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
