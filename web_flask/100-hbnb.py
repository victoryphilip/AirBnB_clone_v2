#!/usr/bin/python3
#<<<<<<< HEAD
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
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
from models import amenity
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
#>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
#<<<<<<< HEAD
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('100-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
#=======
    """
        Flask route at /hbnb.
        Fills the hbnb homepage.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    values = {"states": states, "amenities": amenities, "places": places}
    return render_template('100-hbnb.html', **values)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
#>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
