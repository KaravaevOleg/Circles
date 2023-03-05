import app
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
import jwt
from app.models import User
from app.config.config import Config

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    # Находим пользователя в базе данных
    user = User.objects(email=email).first()

    if user and check_password_hash(user.password, password):
        # Создаем jwt-токен
        token_payload = {"email": email}
        token = jwt.encode(token_payload, app.config["SECRET_KEY"], algorithm="HS256").decode("utf-8")

        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401