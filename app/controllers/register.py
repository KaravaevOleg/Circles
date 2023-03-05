import app
from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime
from app.config.config import Config
from app.models import Users

register_bp = Blueprint('register', __name__)


@register_bp.route("/register", methods=["POST"])
def register():
    name = request.json.get("name")
    surname = request.json.get("surname")
    email = request.json.get("email")
    password = request.json.get("password")
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()

    # Создаем объект класса User
    user = Users(name=name, surname=surname, email=email, password=password, created_at=created_at, updated_at=updated_at)

    # Сохраняем пользователя в базу данных
    user.save()

    # Создаем jwt-токен
    token_payload = {"email": email}
    token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm="HS256").encode("utf-8")

    return jsonify({"token": token}), 200

