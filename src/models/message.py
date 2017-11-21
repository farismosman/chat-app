from src import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'), nullable=False)
    chat = db.relationship('Chat', backref=db.backref('messages', lazy=True))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, text, chat, created_by):
        self.text = text
        self.chat = chat
        self.created_by = created_by

    def __repr__(self):
        return '<Message %s>'.format(self.text)
