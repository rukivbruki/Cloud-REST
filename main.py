from flask import Flask, request
from helpers import init_stack
from models import call_numequalto, call_set, call_unset, call_undo, call_redo, call_end, call_get

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get():
    name = request.args.get('name')

    return call_get(name)


@app.route('/numequalto', methods=['GET'])
def numequalto():
    value = request.args.get('value')

    return call_numequalto(value)


@app.route('/set', methods=['GET'])
def set():
    name = request.args.get('name')
    value = request.args.get('value')
    operations_name = request.endpoint

    return call_set(name, value, operations_name)


@app.route('/unset', methods=['GET'])
def unset():
    name = request.args.get('name')
    operations_name = request.endpoint

    return call_unset(name, operations_name)


@app.route('/undo', methods=['GET'])
def undo():
    return call_undo()


@app.route('/redo', methods=['GET'])
def redo():
    return call_redo()


@app.route('/end', methods=['GET'])
def end():
    return call_end()


if __name__ == '__main__':
    init_stack()
    app.run(host='127.0.0.1', port=8080, debug=True)
