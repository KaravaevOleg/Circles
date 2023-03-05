from flask import Flask
from app.config.config import Config
from app.controllers.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()