#!/usr/bin/python3
from flask import Flask
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
    """Rendering html"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
