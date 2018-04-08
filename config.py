# Generic config options for this application

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 

class Config(object):
    
    HOST = "172.16.16.21"
    
    # SQLAlchemy config
    
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://scpuser:alabamanigger@localhost:3306/scp'

class DevelopmentConfig(Config):
    DEBUG = True
    HOST="localhost"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
