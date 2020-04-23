#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def print_state():
    """ string to be returned """
    states = storage.all(State).values()
    print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def closesession(self):
    """ string to be returned """
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
