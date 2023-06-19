# from flask import Flask,session,g,render_template, request, redirect, url_for, flash
# import os
# from flask_sqlalchemy import SQLAlchemy
# from flask import send_from_directory
# from flask.cli import with_appcontext
# from datetime import datetime
# import sqlalchemy
# from sqlalchemy import text,desc
# from sqlalchemy.sql import func
# from sqlalchemy.ext.declarative import declarative_base
# from inflection import camelize
# import sys

# app = Flask(__name__)
# app.debug = True
# unknown_folder = "Unknown"

# @app.route("/")
# def home():
#     # image_names = os.listdir(unknown_folder)
#     # return render_template("index.html", image_names=image_names)
#     return render_template("index.html")

# @app.route("/login")
# def login():
#     # image_names = os.listdir(unknown_folder)
#     # return render_template("index.html", image_names=image_names)
#     return render_template("login.html")

# @app.route("/signup")
# def signup():
#     # image_names = os.listdir(unknown_folder)
#     # return render_template("index.html", image_names=image_names)
#     return render_template("signup.html")

# @app.route("/images/<path:filename>")
# def serve_image(filename):
#     return send_from_directory(unknown_folder, filename)

# if __name__ == "__main__":
#     app.run()

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

app = Flask(__name__)

app.secret_key = 'xyzsdfg'

loginmain=False

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
            return render_template('index.html', mesage = mesage)
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
    
@app.route('/registerbuttonmain')
def registerbuttonmain():
    if loginmain==True:
        known_dir = "Known"
        subfolder_name = "Guru"  # Change this to the desired subfolder name

        # Create the subfolder if it doesn't exist
        subfolder_path = os.path.join(known_dir, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

        # Initialize webcam
        video_capture = cv2.VideoCapture(0)

        # Face detection parameters
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Counter to keep track of the number of captured images
        image_counter = 0

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw bounding boxes around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting image
            cv2.imshow('Collecting Faces', frame)

            # Capture and save face images when 's' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('s') and len(faces) == 1:
                # Increment the image counter
                image_counter += 1

                # Save the face image
                face_image_path = os.path.join(subfolder_path, f"{image_counter}.jpg")
                cv2.imwrite(face_image_path, frame)

                print(f"Captured image {image_counter}")

            # Exit loop when 50 images are captured or 'q' is pressed
            if image_counter >= 100 or cv2.waitKey(1) & 0xFF == ord('q'):
                break
            print("Here")
        # Release the webcam and destroy the windows
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        return 'You have not logged in'

def home():
    image_names = os.listdir(unknown_folder)
    return render_template("index.html", image_names=image_names)
    # return render_template("login.html")

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(unknown_folder, filename)

if __name__ == "__main__":
    app.run()