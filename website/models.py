from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class UserHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_description = db.Column(db.String(255))
    activity_date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('user_history', lazy=True))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    history = db.relationship('UserHistory')
