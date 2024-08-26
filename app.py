#!/usr/bin/python3
#imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app configuration for sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mycareerdatabse.db'
database = SQLAlchemy(app)

# Home page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ in "__main__":
    app.run(debug=True)