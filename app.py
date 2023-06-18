from flask import Flask,session,g,render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
from flask.cli import with_appcontext
from datetime import datetime
import sqlalchemy
from sqlalchemy import text,desc
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from inflection import camelize
import sys

app = Flask(__name__)
app.debug = True
unknown_folder = "Unknown"

@app.route("/")
def home():
    image_names = os.listdir(unknown_folder)
    return render_template("index.html", image_names=image_names)
    # return render_template("login.html")

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(unknown_folder, filename)

if __name__ == "__main__":
    app.run()