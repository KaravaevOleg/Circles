from flask_mongoengine import MongoEngine
from config import Config

db = MongoEngine()


def init_app(app):
    app.config.from_object(Config)
    db.init_app(app)
