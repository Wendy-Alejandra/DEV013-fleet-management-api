"""Taxi model"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Taxi(db.Model):
    """Create Taxi class"""
    __tablename__ = "taxis"

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
