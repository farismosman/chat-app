from src import app
from src import User, Chat
from flask import request, Response, json


@app.route('/chat/start', methods=['POST'])
def create():
    auth_token = request.headers['Authorization']
    authorized = User.is_authorized(auth_token)

    if authorized:
        user_id = User.decode(auth_token)
        chat_id = Chat.create(user_id)

        return Response(json.dumps({'chat_id': chat_id}), status=201, mimetype='application/json')
    else:
        return Response(status=401, smimetype='application/json')

@app.route('/chat/<id>', methods=['GET'])
def get(id):
    auth_token = request.headers['Authorization']
    authorized = User.is_authorized(auth_token)

    if authorized:
        try:
            user_id = User.decode(auth_token)
            chat = Chat.get(id, user_id)

            return Response(json.dumps({
                    'id': chat.id,
                    'messages': chat.messages
                    }),
                    status=200, mimetype='application/json')
        except:
            return Response(status=404, mimetype='application/json')
    else:
        return Response(status=401, smimetype='application/json')