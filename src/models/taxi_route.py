"""Defining taxis routes"""
from flask import Blueprint, jsonify
from flask import request
from src.models.models import Taxi

taxi_bp = Blueprint("taxi_bp", __name__)

@taxi_bp.route("/taxis", methods=["GET"])
def get_taxis():
    """Get list of taxis and pagination
    ---
    parameters:
      - name: query
        in: query
        type: string
        required: false
        description: taxi plate.

      - name: page
        in: query
        type: integer
        required: false
        description: result page number. The default value is 1.

      - name: limit
        in: query
        type: integer
        required: false
        description: Number of elements per page. The default value is 10.

    responses:
      200 :
        description: Returns a list of taxis in JSON format.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: taxi ID.
              plate:
                type: string
                description: taxi plate.
    """
    try:
        # Filtering the data from db per page using request parameters
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)
        # using Flask SQLAlchemy pagination object all arguments to paginate are keyword-only
        # .items on the current page list (as paginate() is an object so it is not iterable)
        taxis = Taxi.query.paginate(page=page, per_page=per_page,error_out=False).items
        print(taxis)

        # Build list of taxis
        taxi_list = [{"id": taxi.id, "plate": taxi.plate} for taxi in taxis]
        return jsonify(taxi_list)
    except Exception as e:
        return jsonify({"message": str(e)}), 500
