from src import db
from datetime import datetime

class Chat(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    participant = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, created_by, participant):
        self.created_by = created_by
        self.participant = participant

    def __repr__(self):
        return '<Chat %s>'.format(self.id)

    @staticmethod
    def create(user_id, participant):
        chat = Chat(user_id, participant)
        db.session.add(chat)
        db.session.commit()

        return chat.id


    @staticmethod
    def get(chat_id, user_id):
        chat = Chat.query.filter(and_(Chat.id==chat_id, or_(Chat.created_by==user_id, Chat.participant==user_id))).first()
        if chat:
            return chat

        raise Exception('No chat found')