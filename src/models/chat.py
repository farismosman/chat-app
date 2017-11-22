from src import db
from datetime import datetime

class Chat(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, created_by):
        self.created_by = created_by

    def __repr__(self):
        return '<Chat %s>'.format(self.id)

    @staticmethod
    def create(user_id):
        chat = Chat(user_id)
        db.session.add(chat)
        db.session.commit()

        return chat.id

