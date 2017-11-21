import json
from src import app, db
from src import User
from flask import request, Response


@app.route('/user/register', methods=['POST'])
def register():
    data = json.loads(request.data)

    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    password = data['password']

    user = User(first_name, last_name, username, password)
    db.session.add(user)

    return Response(status=201, mimetype='application/json')