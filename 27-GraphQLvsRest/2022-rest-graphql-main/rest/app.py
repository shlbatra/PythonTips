"""Rest Interface using flask
Not good about design -
- directly returning results from opns such as get blog and update blog -> Security Issue
"""

from flask import Flask, jsonify, request

from data import all_authors, all_blogs, get_author, get_blog, update_blog

app = Flask(__name__)


@app.route("/")
def route_hello_world():
    return "Hello, World!"

#root route
@app.route("/blogs")
def route_all_blogs():
    return jsonify(all_blogs())


@app.route("/blogs/<id>", methods=["GET"])
def route_get_blog(id: str):
    return jsonify(get_blog(int(id)))

"""
curl -X POST -H "Content-Type: application/json" \
-d '{"title": "I like this blog"}' \
http://127.0.0.1:5000/blogs/2
"""

@app.route("/blogs/<id>", methods=["POST"])
def route_update_blog(id: str):
    data = request.get_json()
    return jsonify(update_blog(int(id), data))

@app.route("/authors")
def route_all_authors():
    return jsonify(all_authors())


@app.route("/authors/<id>")
def route_get_author(id: str):
    return jsonify(get_author(int(id)))


if __name__ == "__main__":
    app.run(debug=True)
