"""sqlalchemy set up"""
# Flask class. Instance of this class will be our WSGI application (Web Server Gateway Interface).
import os
from flask_sqlalchemy import SQLAlchemy

# db from SQLAlchemy class imported from flask_sqlalchemy
db = SQLAlchemy()
class Config():
    """SQLAlchemy configuration"""
    # Configure the SQLAlchemy database
    postgres_url = os.getenv('POSTGRES_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Get URI connection to PostgreSQL from environment variables
    SQLALCHEMY_DATABASE_URI = postgres_url
