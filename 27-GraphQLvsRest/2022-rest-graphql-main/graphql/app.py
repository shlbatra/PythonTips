from ariadne import \
    graphql_sync  # wrapper lib to define graphql server with graphql types
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, jsonify, request

from schema.create import create_schema

app = Flask(__name__)

#Only 2 routes defined gere -> GET AND POST
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

#main graphql interface - boilerplate code not change
@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    schema = create_schema()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)
