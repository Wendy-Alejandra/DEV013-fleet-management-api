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
    """Index route"""
    return "Welcome to the Fleet Management API!"

@app.route("/taxis", methods=["GET"])
def get_taxis():
    """Get list of taxis and pagination"""
    # Obtener los parámetros de consulta de la URL
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)

    # Calcular el índice de inicio y fin de los elementos
    start_index = (page - 1) * per_page
    print(start_index)
    end_index = start_index + per_page
    print(end_index)

    # Si es la página 2, solo devolver 5 elementos en total
    if page == 2:
        start_index = 0
        per_page = 5

    # Consultar la base de datos solo para los taxis de la página actual
    taxis = Taxi.query.offset(start_index).limit(per_page).all()
    print(taxis)

    # Construir la lista de taxis
    taxi_list = [{"id": taxi.id, "plate": taxi.plate} for taxi in taxis]
    return jsonify(taxi_list)

    # taxis = Taxi.query.all()
    # Limiting the number of elements per page
    # limit = int(request.args.get('limit', 5))
    # taxis = Taxi.query.limit(limit).all()
    # if not "/taxis":
    #     return jsonify({"error": "No taxis found"}), 404
    # print(taxis)
    # taxi_list = [{"id": taxi.id, "plate": taxi.plate} for taxi in taxis]
    # return jsonify(taxi_list)


# If the name of the app from main route __main__ then execute our app with the run() cmd
if __name__ == "__main__":
    app.run(debug=True, port=5000) # Debugger activated
