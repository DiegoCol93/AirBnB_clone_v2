#!/usr/bin/python3
# Sets a basic flask server.
from flask import Flask, escape, request


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
