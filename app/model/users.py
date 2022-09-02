from ..utils.db import db
from flask import jsonify
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    passw = db.Column("pass",db.String(500), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    def __init__(self, id,username,passw,email):
         self.id=id
         self.username=username
         self.passw=passw
         self.email=email

    def __str__(self):
        return "username: {"+self.username+"} email:{"+self.email+"}"


