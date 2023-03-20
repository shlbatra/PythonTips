"""
API calls db
Once get response from database, we jsonify before returning final output on web
"""

from flask import Flask, abort, jsonify

from db import fetch_blog, fetch_blogs

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/blogs')
def all_blogs():
    return jsonify(fetch_blogs())

@app.route('/blogs/<id>')
def get_blog(id):
        return jsonify(fetch_blog(id))

app.run()
