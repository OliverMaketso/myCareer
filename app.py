#!/usr/bin/python3
#imports
from flask import Flask, render_template, redirect, request, flash, url_for
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user

app = Flask(__name__)

# app configuration for sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mycareerdatabse.db'
database = SQLAlchemy(app)

bcrypt = Bcrypt(app)


# data class - rows of data Table
class user(database.Model):
    __tablename__ = 'user'

    user_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    surname = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(255), nullable=False)
    password = database.Column(database.String(50), nullable=False)
    created_at = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"User {self.id}"


# Home page
@app.route("/")
def index():
    return render_template("landingpage.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = user(name=name, surname=surname, email=email, password=hashed_password)
        database.session.add(new_user)
        database.session.commit()
        flash('Your account has been created!', 'Success')
        return redirect(url_for("login"))
    return render_template('signup.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        account = user.query.filter_by(email=email).first()
        if account and bcrypt.check_password_hash(user.password, password):
            login_user(account)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, incorrect email or password')
    return render_template('login.html')


@app.route('/careers', methods=['GET'])
def careers():
    return render_template('careers.html')


@app.route('/freecourses', methods=['GET'])
def freecourses():
    return render_template('freecourses.html')


@app.route('/recommanded', methods=['GET'])
def recommanded():
    return render_template('recommanded.html')

if __name__ in "__main__":
    with app.app_context():
        database.create_all()
    
    app.run(debug=True)