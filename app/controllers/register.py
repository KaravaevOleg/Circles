import app
from flask import Blueprint, request, jsonify
import jwt
from app.config.config import Config
from app.models import User

register_bp = Blueprint('auth', __name__)


@register_bp.route("/register", methods=["POST"])
def register():
    name = request.json.get("name")
    surname = request.json.get("surname")
    email = request.json.get("email")
    password = request.json.get("password")

    # Создаем объект класса User
    user = User(name=name, surname=surname, email=email, password=password)

    # Сохраняем пользователя в базу данных
    user.save()

    # Создаем jwt-токен
    token_payload = {"email": email}
    token = jwt.encode(token_payload, app.config["SECRET_KEY"], algorithm="HS256").decode("utf-8")

    return jsonify({"token": token}), 200

