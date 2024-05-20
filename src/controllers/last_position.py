"""Defining last position endpoint for each taxi"""
from flask import Blueprint, jsonify, request
from sqlalchemy import func, and_
from sqlalchemy.exc import SQLAlchemyError
from src.models.models import Trajectory, Taxi

last_position_bp = Blueprint("last_position", __name__)

@last_position_bp.route("/trajectories/latest", methods=["GET"])
def get_last_position():
    """Get last position for each taxi"""
    try:
        # Pagination limits
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        # Subquery to get last position per taxi
        latest_subquery = Trajectory.query.with_entities(
            Trajectory.taxi_id,
            func.max(Trajectory.date).label('max_date')
        ).group_by(Trajectory.taxi_id).subquery()

        # Main query with pagination included
        latest_trajectories = Trajectory.query.join(Taxi, Trajectory.taxi_id == Taxi.id)\
            .join(latest_subquery, and_(
                Trajectory.taxi_id == latest_subquery.c.taxi_id,
                Trajectory.date == latest_subquery.c.max_date
            ))\
            .with_entities(Trajectory.taxi_id,
                Taxi.plate,
                Trajectory.latitude,
                Trajectory.longitude,
                Trajectory.date)\
            .distinct(Trajectory.taxi_id)\
            .paginate(page=page, per_page=per_page,error_out=False).items

        # Customized message if not elements in the page
        if not latest_trajectories:
            return jsonify({"message": "No trajectories found"}), 404

        # Convert results to JSON
        trajectories_jason = []
        for trajectory in latest_trajectories:
            trajectory_dict = {
                'taxi_id': trajectory[0],
                'plate': trajectory[1],
                'latitude': trajectory[2],
                'longitude': trajectory[3],
                'timestamp': trajectory[4].strftime('%Y-%m-%d %H:%M:%S')
            }
            trajectories_jason.append(trajectory_dict)
        return jsonify(trajectories_jason)

    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "message": str(e)}), 500
