import os

from extensions import db
from flask import Flask
from views import register_views


def register_extensions(app):
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get('SETTINGS'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_extensions(app)
    register_views(app)

    return app
