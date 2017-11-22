import json
from src import app
from src import User
from flask import request, Response, json


@app.route('/user/register', methods=['POST'])
def register():
    data = json.loads(request.data)

    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    password = data['password']

    token = User.register(first_name, last_name, username, password)

    return Response(json.dumps({'auth_token': token}), status=201, mimetype='application/json')

@app.route('/user/login', methods=['POST'])
def login():
    data = json.loads(request.data)

    username = data['username']
    password = data['password']

    token = User.authenticate(username, password)

    return Response(json.dumps({'auth_token': token}), status=200, mimetype='application/json')