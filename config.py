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
    
    
class ProdConfig(Config):
    ''' Production configuration child class
    
    Args:
        config: the parent configuration class with General configuration settings
        '''
    SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')
    
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    ENV = 'development'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

        