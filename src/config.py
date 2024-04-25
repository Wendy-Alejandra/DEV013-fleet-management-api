"""sqlalchemy set up"""
# Flask class. Instance of this class will be our WSGI application (Web Server Gateway Interface).
import os
from flask_sqlalchemy import SQLAlchemy

# db from SQLAlchemy class imported from flask_sqlalchemy
db = SQLAlchemy()
class Config():
    """SQLAlchemy configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Configure SQLAlchemy database & Get URI connection to PostgreSQL from env variables
    SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRES_URL')
