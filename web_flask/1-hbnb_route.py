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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
