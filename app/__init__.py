from flask import Flask
from app.config.config import Config
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from app.controllers.register import register_bp
from app.controllers.auth import auth_bp

mongo = PyMongo()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Импорт и регистрация контроллеров Flask
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
    return app
