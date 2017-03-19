from flask import Flask
from os import environ


def create_app(name=__name__):
    app = Flask(name)

    env = environ.get('APP_ENV', 'dev')
    app.config.from_object(
        '{}.settings.{}Config'.format(name, env.capitalize()))
    app.config['ENV'] = env

    from .models import mongo
    mongo.init_app(app)

    from .routes import api
    app.register_blueprint(api, url_prefix='/api/v1')

    return app
