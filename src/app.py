"""Flask application"""
import os
from flask import Flask
from flasgger import Swagger
from src.config import config
from src.models.models import db
from src.models.taxi_route import taxi_bp
from src.models.trajectory_route import trajectory_bp
from src.models.last_position import last_position_bp

def create_app():
    """Create Flask Application"""
    # Instance of Flask class. Argument __name__ is the name of the application’s module or package.
    app = Flask(__name__)
    app.config.from_object(config[os.getenv('ENVIRONMENT')]) # calling development mode from the dictionary

    # initialize the SQLAlchemy extension class with the application by calling :
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(taxi_bp)
    app.register_blueprint(trajectory_bp)
    app.register_blueprint(last_position_bp)

    # Initialize Swagger
    Swagger(app)

    return app

# @app.route("/")
# def index():
#     """Index route"""
#     return "Welcome to the Fleet Management API!"

# If the name of the app from main route __main__ then execute our app with the run() cmd
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000) # Debugger activated
