from flask import Flask,session,g,render_template, request, redirect, url_for, flash
import os
import re
import cv2
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
from flask.cli import with_appcontext
from datetime import datetime
import sqlalchemy
from sqlalchemy import text,desc
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
# from inflection import camelize
import sys
from flask_mysqldb import MySQL
import MySQLdb.cursors
import Data_Collection
import Encoder

app = Flask(__name__)

app.secret_key = 'xyzsdfg'

loginmain=False
subfoldername=""

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'

mysql = MySQL(app)

app.debug = True
unknown_folder = "Unknown"


@app.route("/")
@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    global loginmain
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            loginmain=True
            return redirect(url_for('index'))
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
@app.route('/logout')
def logout():
    global loginmain
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    loginmain=False
    return redirect(url_for('login'))
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

@app.route('/index', methods =['GET', 'POST'])
def index():
    global loginmain
    if loginmain==True:
        return render_template("index.html")
    else:
        return redirect(url_for('login'))
    # return render_template("login.html")

@app.route('/process_input', methods=['POST'])
def process_input():
    global subfoldername
    data = request.get_json()
    name = data.get('name')
    subfoldername=name
    print(subfoldername)
    return name

@app.route('/registerbuttonmain')
def registerbuttonmain():
    if loginmain==True:
        if subfoldername!="":
            # delete the pickle file
            delete_file = "known_faces.pickle"
            if os.path.exists(delete_file):
                os.remove(delete_file)
            Data_Collection.collect_data(subfoldername)
            Encoder.run_this()
            return 'Succesfully registered'
        else:
            return render_template("index.html")
    else:
        return redirect(url_for('login'))

@app.route('/check_log', methods =['GET', 'POST'])
def check_log():
    global loginmain
    if loginmain==True:
        image_names = os.listdir(unknown_folder)
        return render_template("log.html", image_names=image_names)
    else:
        return redirect(url_for('login'))

@app.route("/images/<path:filename>", methods =['GET', 'POST'])
def serve_image(filename):
    global loginmain
    if loginmain==True:
        return send_from_directory(unknown_folder, filename)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)