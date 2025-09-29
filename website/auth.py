from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import conn

auth = Blueprint('auth', __name__)
cursor = conn.cursor(dictionary=True)

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        ID = request.form.get('ID')

        query = '''
            SELECT student_id, student_email 
            FROM student 
            WHERE student_email = %s AND student_id = %s
        '''
        cursor.execute(query, (email, ID))
        account = cursor.fetchall()

        if account:
            return redirect(url_for('views.home', role='student'))
        else:
            flash("Sai ID hoặc Email, vui lòng thử lại!")

    return render_template('login.html')
