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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
