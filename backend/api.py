from flask import Flask, render_template, jsonify

import os

static_path = os.path.abspath('.') + os.path.sep + 'templates' + os.path.sep + 'assets'

app = Flask(__name__, static_folder=static_path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/users')
def users():
    users = [{'id': 1, 'name': 'user1'}, {'id': 2, 'name': 'user2'}]
    return jsonify(users)
