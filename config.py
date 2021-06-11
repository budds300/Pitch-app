import os

class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:budds300@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    # email configurations
    
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
class TestConfig(Config):
    
    '''
    Testing configuration child class
    
    Args:
        Config: the parent configuration class with general configuration settings
    
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:budds300@localhost/pitch_test'