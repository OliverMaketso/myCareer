#!/usr/bin/python3
#imports
from flask import Flask, render_template, redirect, request, flash, url_for
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user
import re
import requests 

app = Flask(__name__)

# app configuration for sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mycareerdatabase.db'
app.config['SECRET_KEY'] = 'Tshepiso'
database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

#REGEX to validate an email
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# password complexity requirements to be met by each password
def validate_password(password):
    if len(password) < 8:
        return False, "password must be at least 8 characters long!"
    if not re.search(r"[A-Z]", password):
        return False, "password must contain atleast one uppercase!"
    if not re.search(r"[a-z]", password):
        return False, "password must contain atleast one lowercase!"
    if not re.search(r"[0-9]", password):
        return False, "password must contain atleast one number!"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain atleast one special symbol!"
    return True, ""

# data class - rows of data Table
class user(database.Model):
    __tablename__ = 'user'

    user_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    surname = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(255), nullable=False, unique=True)# email uniqueness prevents duplicate accounts
    password = database.Column(database.String(255), nullable=False) #increase the length to accomodate longer hashes
    created_at = database.Column(database.DateTime, default=datetime.utcnow)

#    def __repr__(self) -> str:
#        return f"User {self.id}"

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'surname': self.surname,
            'email': self.emal,
            'password': self.password
        }


class Career(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    description = database.Column(database.Text, nullable=False)
    requirements = database.Column(database.Text, nullable=False)

class Course(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    course_provider = database.Column(database.String(100), nullable=False)
    description = database.Column(database.Text, nullable=False)
    time_to_complete = database.Column(database.Text, nullable=False)
    link = database.Column(database.Text, nullable=False)

# Create the database and table
with app.app_context():
    database.create_all()

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
    #careers = Career.query.all()
    return render_template('careers.html', careers=Career.query.all())


@app.route('/freecourses', methods=['GET'])
def freecourses():
    return render_template('freecourses.html', courses=Course.query.all())


@app.route("/career_list")
def career_list():
    API_KEY = '91e7bcca5f07d95dbf540d18d41e1033'
    API_ID = '501f4066'
    URL = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={API_ID}&app_key={API_KEY}"
    response = requests.get(URL)
    job_data = response.json()['results']
    
    return render_template('career_list.html', jobs=job_data)


# career details page
@app.route('/careers/<int:career_id>')
def career_detail(career_id):
    career = Career.query.get_or_404(career_id)
    return render_template('career_detail.html', career=career)


@app.route('/courses/<int:course_id>')
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course_detail.html', course=course)

#@app.route('/recommended', methods=['GET']) # corrected recommanded to recommended
#def recommanded():
#    return render_template('recommended.html') # corrected recommanded to recommended

if __name__ in "__main__":
    with app.app_context():
        database.create_all()
    
    app.run(debug=True)