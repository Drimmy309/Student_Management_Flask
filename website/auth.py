from flask import Flask, Blueprint, render_template, request, redirect, url_for
import mysql.connector
auth = Blueprint('auth', __name__)

# Database Connection.
conn = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="quanganh309!",
    database="mydb"
)
cursor = conn.cursor()

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ID = request.form.get('ID')
        email = request.form.get('email')
        query = '''SELECT student_id, student_email 
                 FROM student 
                 WHERE student_id = %s AND student_email = %s'''
        cursor.execute(query, (ID, email)) 
        account = cursor.fetchall()
        if account:
            redirect(url_for('views.home', role='student'))

    return render_template('login.html')
