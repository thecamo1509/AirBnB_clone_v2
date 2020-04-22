#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This is the hello function"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_world():
    """This is the HBNB function"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ string"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text='is cool'):
    """ string """
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ Integer """
    return '{} is a number'.format(n).replace('_', ' ')


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_template(n):
    """ string to be returned """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_odd_or_even(n):
    """ string to be returned """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def print_state():
    """ string to be returned """
    state = storage.all('State')
    namedic = {}
    for i in state:
        j = i.to_dict()
        namedic.setdefault(j["name"], j["id"])
    return render_template('7-states_list.html', states=namedic)


@app.teardown_appcontext
def closesession(self):
    """ string to be returned """
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
