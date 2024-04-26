"""Flask application"""
from flask import Flask, jsonify
from flask import request
from flasgger import Swagger
from src.models.taxi_model import db, Taxi
from src.config import Config

# Instance of Flask class. Argument __name__ is the name of the application’s module or package.
app = Flask(__name__)
app.config.from_object(Config())

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

# If the name of the app from main route __main__ then execute our app with the run() cmd
if __name__ == "__main__":
    app.run(debug=True, port=5000) # Debugger activated
