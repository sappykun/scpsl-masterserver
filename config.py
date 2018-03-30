# Generic config options for this application

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 

class Config(object):
    
    HOST = "yourhost.here.com"
    PORT = 80
    
    # SQLAlchemy config
    
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost:3306/database'

class DevelopmentConfig(Config):
    DEBUG = True
    HOST="localhost"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
