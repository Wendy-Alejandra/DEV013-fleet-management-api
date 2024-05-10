"""sqlalchemy environments set up"""
# Flask class. Instance of this class will be our WSGI application (Web Server Gateway Interface).
import os
from flask_sqlalchemy import SQLAlchemy

# db from SQLAlchemy class imported from flask_sqlalchemy
db = SQLAlchemy()
class Config(object):
    """SQLAlchemy base config (common config for all environments)"""
    # Detects any modification to the models' objects in models and executes additional
    # actions to the db such as creating, updating or deleting the objects
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development environment set up"""
    DEVELOPMENT = True
    DEBUG = True
    # Configure SQLAlchemy database & Get URI connection to PostgreSQL from env variables
    SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRES_URL')

class TestingConfig(Config):
    """Testing environment set up"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:/Users/Wendy/db1"

# This dictionary facilitates the access to the available configurations set in this file
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
