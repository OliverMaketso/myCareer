from flask_sqlalchemy import SQLAlchemy
from app import database
from datetime import datetime

class user(database.Model):
    user_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    surname = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(255), nullable=False)
    password = database.Column(database.String(50), nullable=False)
    created_at = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"User {self.id}"
