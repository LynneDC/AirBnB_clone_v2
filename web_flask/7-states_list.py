#!/usr/bin/python3
""" 7. Start flask service that does something. """

from flask import Flask
from flask import render_template
from models import storage
from models.state import state


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(foo):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
