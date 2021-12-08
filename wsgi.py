from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/<name>')
def say(name):
    return f'Hello, {name}!'
    # return f'Hello, {escape(name)}!'
