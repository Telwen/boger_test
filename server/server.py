from flask import Flask, jsonify, request
from to_do_list import todos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/to_do', methods=['GET'])
def to_do():
    return jsonify(todos)

@app.route('/to_do', methods=['POST'])
def tset():
    res = request.json
    id = res['id']
    for args in todos:
        if args['id'] == id:
            args['tdl'].clear()
            for tdls in res['tdl']:
                args['tdl'].append(tdls)
    return jsonify(request.json)


if __name__ == '__main__':
    app.run()

