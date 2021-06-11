from . import db 
from app import create_app,db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from datetime import datetime
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(225))
    
    
    
    def __repr__(self):
        return f'User {self.username}'