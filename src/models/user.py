import jwt, datetime
from src import db, bcrypt, app
from datetime import datetime as dt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.utcnow)

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.id)

    def issue_token(self):
        payload = {
            'expires_at': str(datetime.datetime.utcnow() + datetime.timedelta(days=1)),
            'issued_at': str(datetime.datetime.utcnow()),
            'subject': self.id
            }

        auth_token = jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256')
        return auth_token

    @staticmethod
    def decode(auth_token):
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['subject']

    @staticmethod
    def register(first_name, last_name, username, password):
        user = User(first_name, last_name, username, password)
        db.session.add(user)
        db.session.commit()

        auth_token = user.issue_token()
        return auth_token

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash:
            auth_token = user.issue_token()
            return auth_token
        else:
            raise Exception('Unauthorized')

    @staticmethod
    def is_authorized(auth_token):
        return True if User.decode(auth_token) else False
