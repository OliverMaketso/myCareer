#!/usr/bin/python3
#imports
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
import sql

app = Flask(__name__)

# app configuration for sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mycareerdatabse.db'
database = SQLAlchemy(app)

######## Ignore, contetnts in sql.py file #######
'''
# data class - rows of data Table
class user(database.Model):
    user_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    surname = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(255), nullable=False)
    password = database.Column(database.String(50), nullable=False)
    created_at = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"User {self.id}"
'''

# Home page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ in "__main__":
    with app.app_context():
        database.create_all()
    
    app.run(debug=True)