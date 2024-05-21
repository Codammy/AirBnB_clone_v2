#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, state
app = Flask(__name__)
states = storage.all(state.State)


@app.route('/states_list', strict_slashes=False)
def states_route():
    """renders lists of states from database"""
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def end_db_conn(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
