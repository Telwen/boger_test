from flask import Flask, jsonify, request
from to_do_list import list1
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/to_do', methods=['GET'])
def to_do():
    return jsonify(list1)

@app.route('/to_do', methods=['POST'])
def tset():
    b = request.json
    print(b)
    return jsonify(request.json)


if __name__ == '__main__':
    app.run()
