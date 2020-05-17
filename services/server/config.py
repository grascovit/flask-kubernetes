import os
import secrets


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_urlsafe(32))
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@postgres:{}/flask_postgres_kubernetes'.format(
        os.environ.get('POSTGRES_USER'),
        os.environ.get('POSTGRES_PASSWORD'),
        os.environ.get('POSTGRES_PORT')
    )


class Production(Config):
    ENV = 'production'


class Staging(Config):
    ENV = 'staging'
    DEBUG = True


class Development(Config):
    ENV = 'development'
    DEBUG = True


class Testing(Config):
    ENV = 'test'
    TESTING = True
