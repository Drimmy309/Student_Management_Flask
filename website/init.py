from flask import Flask
from website.auth import auth
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'quang anh dep trai vocolo'
    app.register_blueprint(auth)
    return app
