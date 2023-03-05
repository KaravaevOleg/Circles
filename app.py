from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from app.db import db
import app
from app.controllers.auth import auth_bp
from app.controllers.register import register_bp
from app.controllers.register import register_bp
from app.controllers.base import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
    return app


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#
#     db.init_app(app)
#
#     jwt = JWTManager(app)
#
#     app.register_blueprint(auth_bp)
#     app.register_blueprint(register_bp)
#
#     return app
#
#
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
