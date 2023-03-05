from app import db


class User(db.Document):
    name = db.StringField(required=True)
    surname = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    created_at = db.DateTimeField(required=True)
    updated_at = db.DateTimeField(required=True)