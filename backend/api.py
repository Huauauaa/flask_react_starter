from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/users')
def users():
    users = [{'id': 1, 'name': 'user1'}, {'id': 2, 'name': 'user2'}]
    return jsonify(users)
