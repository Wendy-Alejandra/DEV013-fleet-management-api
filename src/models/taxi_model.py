"""Taxi model"""
from src.config import db

class Taxi(db.Model):
    """Create Taxi class"""
    __tablename__ = "taxis"

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
