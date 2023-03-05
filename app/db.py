from flask_mongoengine import MongoEngine
from config import Config
from flask_mongoengine import Document
from mongoengine.fields import StringField, EmailField, DateTimeField

db = MongoEngine()


def init_app(app):
    app.config.from_object(Config)
    db.init_app(app)
