from pprint import pprint

from flask import Flask, jsonify, request
from to_do_list import todos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    '''
    Users check function.

    Check if user exist. If isn't, create new element in list with entered username.

    Return
    --------------
        None

    '''

    res = request.json
    tdl = todos.get(res["username"])
    if tdl is None:
        todos[res["username"]] = []
    return jsonify({})


@app.route('/todos', methods=['DELETE'])
def delete():
    '''
    Todos delete function.

    Chek todos id and delete it in users todos

    Return
    --------------
        None
    '''
    res = request.args
    headers = request.headers
    tdls = todos.get(headers['Username'])
    tdl_index = None
    for index, tdl in enumerate(tdls):
        if tdl['id'] == int(res['id']):
            tdl_index = index
            break
    tdls.pop(tdl_index)
    return jsonify({})


@app.route('/todos/', methods=['GET'])
def get_todos():
    '''
    Todos get function.

    Get curent user todos list and send it to client.

    Return
    --------------
        tdl
    '''
    res = request.headers
    tdl = todos.get(res["Username"])
    return jsonify(tdl)


@app.route('/to_do', methods=['POST'])
def post_todos():
    '''
    Todos update function.

    Function received todo witch need to update and current username. At first get current user todos list, after that using
    cycle find necessary todo and update it.

    Return
    --------------
        None
    '''

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
    return jsonify({})


if __name__ == '__main__':
    app.run()
