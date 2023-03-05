from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app.models import User

users_bp = Blueprint('users', __name__)


@users_bp.route("/register", methods=["POST"])
def register():
    name = request.json.get("name")
    surname = request.json.get("surname")
    email = request.json.get("email")
    password = request.json.get("password")
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()

    hashed_password = generate_password_hash(password)

    user = User(name=name, surname=surname, email=email, password=hashed_password, created_at=created_at,
                updated_at=updated_at)

    try:
        user.save()
        return jsonify({"message": "User registered successfully!"}), 200
    except:
        return jsonify({"error": "User already exists in database!"}), 400


@users_bp.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    user = User.objects(email=email).first()

    if user and check_password_hash(user.password, password):
        token_payload = {"email": email}
        token = jwt.encode(token_payload, current_app.config['SECRET_KEY'], algorithm="HS256").decode("utf-8")

        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401
