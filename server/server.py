from pprint import pprint

from flask import Flask, jsonify, request
from to_do_list import todos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/delete', methods=['POST'])
def delete():
    res = request.json
    todos.clear()
    for i in res:
        todos.append(i)
    print(todos)
    return jsonify(request.json)

@app.route('/to_do', methods=['GET'])
def to_do():
    return jsonify(todos)

@app.route('/to_do', methods=['POST'])
def tset():
    res = request.json
    print(res)
    id = res['id']
    title = res['title']
    for args in todos:
        if args['id'] == id:
            args['tdl'].clear()
            for tdls in res['tdl']:
                args['tdl'].append(tdls)
            if args['title'] != title:
                args['title'] = title
    if id >= len(todos):
        todos.append(res)


    pprint(todos)

    return jsonify(request.json)


if __name__ == '__main__':
    app.run()

