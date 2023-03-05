from flask import Flask
from app.config.config import Config
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo

mongo = PyMongo()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Импорт и регистрация контроллеров Flask
    from app.controllers.register import auth_bp
    app.register_blueprint(auth_bp)

    return app
