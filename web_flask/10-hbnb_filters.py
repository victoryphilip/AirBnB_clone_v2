#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
#=======
""" Starts a Flask application related to HBNB. """

from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
#>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
#<<<<<<< HEAD
def hbnb_filter():
    """ HBNB filters """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    return render_template('10-hbnb_filters.html',
                           states=st_ct,
                           amenities=amenities)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
#=======
def hbnb_filters():
    """
        Flask route at /hbnb_filters.
        Fills the two popovers in hbnb homepage.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    values = {"states": states, "amenities": amenities}
    return render_template('10-hbnb_filters.html', **values)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
#>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
