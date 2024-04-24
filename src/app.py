"""Flask application"""


from flask import Flask, jsonify
# from flask import request
from flasgger import Swagger
from src.models.taxi_model import db, Taxi
from src.config import Config

# Instance of Flask class. Argument __name__ is the name of the application’s module or package.
app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)

# Initialize Swagger
Swagger(app)

@app.route("/")
def index():
    """Index route"""
    return "Welcome to the Fleet Management API!"

@app.route("/taxis", methods=["GET"])
@app.route("/taxis/<int:page>", methods=["GET"])
def get_taxis(page=1):
    """Get list of taxis and pagination"""
    # using Flask SQLAlchemy pagination object
    # As of Flask-SQLAlchemy 3.0, all arguments to paginate are keyword-only
    # .items on the current page list (as paginate() is an object so it is not iterable)
    taxis = Taxi.query.paginate(page=page, per_page=10,error_out=False).items
    print(taxis)

    # Build list of taxis
    taxi_list = [{"id": taxi.id, "plate": taxi.plate} for taxi in taxis]
    return jsonify(taxi_list)

# If the name of the app from main route __main__ then execute our app with the run() cmd
if __name__ == "__main__":
    app.run(debug=True, port=5000) # Debugger activated
