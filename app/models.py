from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<user {self.username}>"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1500))