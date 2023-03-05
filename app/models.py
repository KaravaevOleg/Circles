from werkzeug.security import generate_password_hash
from app import db


class Users(db.Document):
    name = db.StringField(required=True)
    surname = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    created_at = db.DateTimeField(required=True)
    updated_at = db.DateTimeField(required=True)

    def save(self, *args, **kwargs):
        self.password = generate_password_hash(self.password)
        super(Users, self).save(*args, **kwargs)