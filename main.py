from flask import Flask, request
from stack import Stack
import ast

app = Flask(__name__, static_url_path='/static')
dataStore = None


@app.route('/')
def root():
    return app.send_static_file("index.html")


@app.route('/stack', methods=['POST', 'GET', "PUT", "DELETE"])
def handle_stack():
    global dataStore
    if request.method == 'GET':
        if not dataStore:
            return {}
        if request.args.get('capacity'):
            return dataStore.get_size()
        elif request.args.get('all'):
            return dataStore.list()
        else:
            return dataStore.top()
    elif request.method == "POST":
        data = request.data.decode("UTF-8")
        data = ast.literal_eval(data)
        dataStore = Stack(int(data.get('capacity')))
        return {'msg': "Success"}
    elif request.method == 'PUT':
        data = request.data.decode("UTF-8")
        data = ast.literal_eval(data)
        if 'val' in data:
            return dataStore.push(data.get('val'))
        return {}
    elif request.method == "DELETE":
        if request.args.get('reset'):
            dataStore = None
            return {}
        else:
            return dataStore.pop()
    return None


if __name__ == "__main__":
    app.run(port=80)
