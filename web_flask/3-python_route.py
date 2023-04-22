#!/usr/bin/python3
'''
    starts a Flask web app.
'''

from flask import Flask

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
