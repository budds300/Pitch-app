from . import db 
from app import create_app,db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from datetime import datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(225))
    password_secure = db.Column(db.String(225))
    email = db.Column(db.String(255),unique = True, index = True, nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch',backref = 'users',lazy = 'dynamic')
    downvotes = db.relationship('Downvote',backref = 'users',lazy = 'dynamic')
    upvotes = db.relationship('Upvote',backref = 'users',lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.password_secure= generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Category:
    '''
    Defines different cartegories of pitches
    '''
    __tablename__ = pitchcategories
    
    id = db.Column(db.Integer,primary_key=True)
    name_of_category = db.Column(db.String(225))
    description = db.Column(db.String(225))
    
    @classmethod
    def get_categies(cls):
        '''
        This function fetches all the categories from the database
        '''
        categories = Category.query.all()
        return categories
    
class Pitch():
    
    __tablename__ = 'pitch'
    
    id = db.Column(db.Integer,primary_key=True)
    pitch = db.Colum(db.String(255))
    category_id = db.Column(db.Integer)
    description = db.Column(db.String(225))
    date = db.Column(db.DateTime, default= datetime.utcnow())
    comments = db.relationship('Comments',backref = 'users',lazy = 'dynamic')
    downvotes = db.relationship('Downvote',backref = 'users',lazy = 'dynamic')
    upvotes = db.relationship('Upvote',backref = 'users',lazy = 'dynamic')
    
    
    def save_pitch(self):
        '''
        function that saves the pictch
        '''
        db.session.add(self)
        db.session.commit
    
    @classmethod
    def get_all_pitches(self):
        ''' 
        Function retrieves queriesthe data returns based on cartegory
        '''
        return Pitch.query.all()
    
    @classmethod
    def get_all_pitches_by_category(cls,category_id):
        ''' 
        Function retrieves queriesthe data returns based on cartegory
        '''
        return Pitch.query.filter_by(category_id = category_id)