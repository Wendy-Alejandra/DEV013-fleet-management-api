"""sqlalchemy set up"""
# Flask class. Instance of this class will be our WSGI application (Web Server Gateway Interface).
import os
from flask_sqlalchemy import SQLAlchemy

# db from SQLAlchemy class imported from flask_sqlalchemy
db = SQLAlchemy()
class Config():
    # Get URI connection to PostgreSQL from environment variables
    postgres_url = os.getenv('POSTGRES_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = postgres_url
    # Configure the SQLAlchemy database, relative to the app instance folder
    # app.config["SQLALCHEMY_DATABASE_URI"] = postgres_url
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize the SQLAlchemy extension class with the application by calling :
    # db.init_app(app)
