#coding:utf-8

from app import db

class User(db.Model):
    __tablename__ = 'User'

    id       = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(64), unique=True, index=True)
    Password = db.Column(db.String(128))
    Age      = db.Column(db.Integer)

    def __init__(self, Username=None, Password=None, Age=None):
        self.Username = Username
        self.Password = Password
        self.Age      = Age

    def __repr__(self):
        return '<User %r>' % self.Username
