#!/usr/bin/python3
# Sets a basic flask server.
""" Module for storing the Flask setup. """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


# Root route. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
@app.route('/')
def hello_HBNB():
    """ Returns the content at Flask's root."""
    return ("Hello HBNB!")


# /hbnb route. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
@app.route('/hbnb/')
def HBNB():
    """ Returns the content at Flask's route /hbnb."""
    return ("HBNB")


# /c/<text> route. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
@app.route('/c/<text>')
def text_route(text):
    """ Returns the content at Flask's route /c/<any text>."""
    text = text.replace("_", " ")
    return ("C " + text)


# /python/<text> route. - - - - - - - - - - - - - - - - - - - - - - - - - - - |
@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """ Returns the content at Flask's route /python/<any text>."""
    text = text.replace("_", " ")
    return ("Python " + text)


# /number/<int:num> route. - - - - - - - - - - - - - - - - - - - - - - - - - -|
@app.route('/number/<int:num>')
def number_route(num):
    """ Returns the content at Flask's route /number/<an int number> """
    return ("{} is a number".format(num))


# /number/<int:num> route. - - - - - - - - - - - - - - - - - - - - - - - - - -|
@app.route('/number_template/<int:num>')
def number_template(num):
    """ Returns the content at Flask's route /number_template/<number> """
    return render_template('5-number.html', num=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
