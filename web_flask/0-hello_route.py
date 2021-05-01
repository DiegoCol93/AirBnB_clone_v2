#!/usr/bin/python3
# Sets a basic flask server.
""" Module for storing the Flask setup. """
from flask import Flask, escape, request


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    """ Returns the content at Flask's root."""
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
