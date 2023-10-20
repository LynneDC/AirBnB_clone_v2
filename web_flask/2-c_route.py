#!/usr/bin/python3
""" mport Flask module form flask
python script that display “Hello HBNB!”
and /hbnb: display "HBNB"
/c/<text>: display “C ” followed by the value of the text variable
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Returns text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Return text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
