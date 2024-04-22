"""Flask application"""
# Flask class. Instance of this class will be our WSGI application (Web Server Gateway Interface).
import os
from flask import Flask, jsonify
from flask import request
from flasgger import Swagger
from models.taxi_model import db, Taxi

# Instance of Flask class. Argument __name__ is the name of the application’s module or package.
app = Flask(__name__)

# Get URI connection to PostgreSQL from environment variables
postgres_url = os.getenv('POSTGRES_URL')

# Configure the SQLAlchemy database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = postgres_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize the SQLAlchemy extension class with the application by calling :
db.init_app(app)

# Initialize Swagger
Swagger(app)

@app.route("/")
def index():
    """
    Index route
    ---
    get:
      description: Returns a welcome message
      responses:
        200:
          description: A welcome message
          schema:
            type: string
    """
    return "Welcome to the Fleet Management API!"

@app.route("/taxis", methods=["GET"])
def get_taxis():
    """
    Get list of taxis
    ---
    swagger: "3.0"
    info:
    description: "Documentation [Fleet Management API - Python](https://github.com/Wendy-Alejandra/DEV013-fleet-management-api/tree/main)"
    version: "1.0.0-basic"
    title: "Fleet management API"
    tags:
    - name: "taxis"
        description: "Taxi operations"
    paths:
    /taxis:
        get:
        summary: "taxis list"
        description: ""
    parameters:
    - name: limit
    in: query
    type: integer
    description: Number of elements per page
    default: 10
    responses:
    200:
        description: A list of taxis (successful operation)
        schema:
        type: array
        items:
            $ref: '#/definitions/Taxi'
    404:
        description: No taxis found
        properties:
            id:
            type: integer
            description: The taxi ID (primary key)
            plate:
            type: string
            description: The taxi plate number (alphanumeric)
    """
    # Limiting the number of elements per page
    limit = int(request.args.get('limit', 5))
    taxis = Taxi.query.limit(limit).all()
    if not "/taxis":
        return jsonify({"error": "No taxis found"}), 404
    print(taxis)
    taxi_list = [{"id": taxi.id, "plate": taxi.plate} for taxi in taxis]
    return jsonify(taxi_list)


# If the name of the app from main route __main__ then execute our app with the run() cmd
if __name__ == "__main__":
    app.run(debug=True, port=5000) # Debugger activated
