from flask import Flask
from .views import user


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=user)
    return app
