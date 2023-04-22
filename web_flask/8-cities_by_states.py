#!/usr/bin/python3
'''
    Starts a Flask web application.
'''

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''
        Returns a list of all cities by state.
    '''
    states = storage.all('State')
    return render_template('8-cities_by_states.html',
                           states=states)


@app.teardown_appcontext
def teardown_db(exception):
    '''
        This is necessary to remove the
        global SQLAlchemy session completely.
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

