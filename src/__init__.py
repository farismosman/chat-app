from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt(app)

POSTGRES = {
    'user': 'chatter',
    'pw': 'Mxwp78RB4rcjKa',
    'db': 'timesmedia',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from models.user import User
from models.message import Message
from models.chat import Chat

import src.views.home
import src.views.user