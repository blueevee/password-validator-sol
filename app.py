from api import app
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, ObjectType
from flask import request, jsonify
from api.queries import verify_resolver


query = ObjectType("Query")
query.set_field("verify", verify_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query
)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    valid_password = result['data']['verify']['verify']
    status_code = 200 if valid_password else 400
    return jsonify(result), status_code