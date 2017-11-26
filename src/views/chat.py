from src import app
from src import User, Chat, Message
from flask import request, Response, json


@app.route('/chat/start', methods=['POST'])
def create():
    auth_token = request.headers['Authorization']
    authorized = User.is_authorized(auth_token)

    if authorized:
        user_id = User.decode(auth_token)
        data = json.loads(request.data)
        participant = data['participant']

        chat_id = Chat.create(user_id, participant)
        body = json.dumps({'chat_id': chat_id})

        return Response(body, status=201, mimetype='application/json')
    else:
        return Response(status=401, smimetype='application/json')


@app.route('/chat/<id>', methods=['GET'])
def get(id):
    auth_token = request.headers['Authorization']
    authorized = User.is_authorized(auth_token)

    if authorized:
        user_id = User.decode(auth_token)
        chat = Chat.get(id, user_id)
        body = json.dumps({'id': chat.id, 'messages': chat.messages})

        return Response(body, status=200, mimetype='application/json')
    else:
        return Response(status=401, smimetype='application/json')


@app.route('/chat/<id>/message', methods=['POST'])
def message(id):
    auth_token = request.headers['Authorization']
    authorized = User.is_authorized(auth_token)

    if authorized:
        user_id = User.decode(auth_token)

        data = json.loads(request.data)
        text = data['text']

        Message.create(text, id, user_id)
        return Response(status=201, mimetype='application/json')
    else:
        return Response(status=401, smimetype='application/json')