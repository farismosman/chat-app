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
app.config['SECRET_KEY'] = '\xb8\xd6F\x15"\x8f\xe7\xb0\xd2\xfedk\x02\xcc#\xea\xa0\xf4\x91\xe7W3\xbev'
db.init_app(app)

from models.user import User
from models.chat import Chat
from models.message import Message, MessageJSONEncoder

app.json_encoder = MessageJSONEncoder

import src.views.home
import src.views.user
import src.views.chat