import os
from . import app


class Config(object):
    SECRET_KEY = 'changeme'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(app.instance_path, 'demo.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
