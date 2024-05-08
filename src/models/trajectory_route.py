"""Defining trajectories endpoint"""
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from src.models.models import Trajectory

trajectory_bp = Blueprint("trajectory_bp", __name__)

@trajectory_bp.route("/trajectories/<int:taxi_id>", methods=["GET"])
def get_trajectories(taxi_id):
    """Get list of taxis trajectories"""
    # Getting date as a query param
    date_str = request.args.get('date')
    print(date_str)

    # Pagination limits
    page = request.args.get('page', default=1, type=int)
    print(page)
    per_page = request.args.get('per_page', default=10, type=int)
    print(per_page)

    if not date_str:
        return jsonify({"error": "date parameter is required"}), 400

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        date_tomorrow = date + timedelta(days=1) # Adds one day to date

    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD format"}), 400

    # Querying trajectories at once
    trajectories = Trajectory.query.filter_by(taxi_id=taxi_id)\
                                   .filter(Trajectory.date.between(date, date_tomorrow))\
                                   .paginate(page=page, per_page=per_page,error_out=False).items

    if not trajectories:
        return jsonify({"message": "No trajectories found for the given taxi_id and date"}), 404

    trajectory_list = [{
        "id": trajectory.id, 
        "taxi_id": trajectory.taxi_id, 
        "date": trajectory.date.isoformat(), 
        "latitude": trajectory.latitude, 
        "longitude": trajectory.longitude
    } for trajectory in trajectories]

    return jsonify(trajectory_list), 200
    