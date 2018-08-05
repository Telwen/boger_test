from pprint import pprint

from flask import Flask, jsonify, request
from to_do_list import todos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    res = request.json
    tdl = todos.get(res["username"])
    if tdl is None:
        todos[res["username"]] = []
    return jsonify({})


@app.route('/delete', methods=['DELETE'])
def delete():
    res = request.args
    headers = request.headers
    tdls = todos.get(headers['Username'])
    tdl_index = None
    for index, tdl in enumerate(tdls):
        if tdl['id'] == int(res['id']):
            tdl_index = index
            break
    tdls.pop(tdl_index)
    return jsonify(request.json)


@app.route('/todos', methods=['GET'])
def get_todos():
    res = request.headers
    tdl = todos.get(res["Username"])
    return jsonify(tdl)


@app.route('/to_do', methods=['POST'])
def post_todos():
    res = request.json
    headers = request.headers
    id = res['id']
    user_tdl = todos.get(headers["Username"])
    if user_tdl is not None:
        is_updated = False

        for args in user_tdl:
            if args['id'] != id:
                continue
            args.update(res)
            is_updated = True

        if not is_updated:
            todos[headers["username"]].append(res)
    return jsonify(request.json)


if __name__ == '__main__':
    app.run()
