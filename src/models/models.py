"""Taxi and Trajectory models"""
from src.config import db
class Taxi(db.Model):
    """Create taxi table class"""
    __tablename__ = "taxis"
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)

class Trajectory(db.Model):
    """Create trajectories table class"""
    __tablename__ = "trajectories"
    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, db.ForeignKey("taxis.id"), nullable=False)
    date = db.Column(db.TIMESTAMP, nullable=False)
    latitude = db.Column(db.DOUBLE_PRECISION, nullable=False)
    longitude = db.Column(db.DOUBLE_PRECISION, nullable=False)
    taxi = db.relationship("Taxi", backref=db.backref("trajectories", lazy=True))
