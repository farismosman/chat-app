from src import db, Chat
from datetime import datetime
from flask.json import JSONEncoder


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'), nullable=False)
    chat = db.relationship('Chat', backref=db.backref('messages', lazy=True))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    db.CheckConstraint('created_by == chat.created_by OR created_by chat.participant')

    def __init__(self, text, chat_id, created_by):
        self.text = text
        self.chat_id = chat_id
        self.created_by = created_by

    def __repr__(self):
        return '<Message %s>'.format(self.text)

    @staticmethod
    def create(text, chat_id, user_id):
        message = Message(text, chat_id, user_id)
        db.session.add(message)
        db.session.commit()


class MessageJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Message):
            return {
                'id': obj.id,
                'text': obj.text,
                'created_by': obj.created_by,
                'created_at': obj.created_at
            }

        return super(MessageJSONEncoder, self).default(obj)