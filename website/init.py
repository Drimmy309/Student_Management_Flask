from flask import Flask
from .auth import auth
from .views import views
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'quang anh dep trai vocolo'
    app.register_blueprint(auth)
    app.register_blueprint(views)
    return app
