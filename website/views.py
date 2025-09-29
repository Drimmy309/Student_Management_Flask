from flask import render_template, Blueprint

views = Blueprint('views', __name__)

@views.route('/home')
def home(role):
    if role == "student":
        return render_template('home.html')