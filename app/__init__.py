from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('app.default_settings.Config')
app.config.from_pyfile('settings.cfg', silent=True)

db = SQLAlchemy(app)
sio = SocketIO(app)

import socket # noqa

from web import web as web_blueprint # noqa
app.register_blueprint(web_blueprint)

from api import api as api_blueprint # noqa
app.register_blueprint(api_blueprint, url_prefix='/api')
