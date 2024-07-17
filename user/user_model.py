from dataclasses import dataclass

from werkzeug.security import generate_password_hash, check_password_hash

from config.db import db


@dataclass
class User(db.Model):
    id: int
    username: str
    password: str
    preferences: dict

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    preferences = db.Column(db.JSON, nullable=True)

    def __init__(self, username, password, preferences=None):
        self.username = username
        self.password = generate_password_hash(password)
        self.preferences = preferences if preferences else {}

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'preferences': self.preferences
        }

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_preferences(self, preferences):
        self.preferences = preferences
        db.session.commit()

    def get_preferences(self):
        return self.preferences
