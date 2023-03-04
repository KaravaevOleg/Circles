from datetime import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client["Circles"]
users = db["users"]


@app.route("/")
def index():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    password = request.form.get("password")
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()

    user = {
        "name": name,
        "surname": surname,
        "email": email,
        "password": password,
        "created_at": created_at,
        "updated_at": updated_at
    }

    try:
        users.insert_one(user)
        return "User registered successfully!"
    except DuplicateKeyError:
        return "User already exists in database!"



if __name__ == "__main__":
    app.run(debug=True)
