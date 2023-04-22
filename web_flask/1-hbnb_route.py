#!/usr/bin/python3
<<<<<<< HEAD
'''
    starts a Flask web app.
'''
=======
""" This is the 2nd Flask setup script. """
>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9

from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
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
=======
@app.route('/', strict_slashes=False)
def hello():
    """
        Flask route at root (http://localhost:5000/).
        Displays 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Flask route at /hbnb (http://localhost:5000/hbnb).
        Displays 'HBNB'.
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
