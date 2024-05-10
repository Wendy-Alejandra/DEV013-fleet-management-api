"""Client configuration"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import create_app
from src.config import config
from src.models.models import Taxi, Trajectory

app = create_app()

@pytest.fixture
def client():
    """Client definition"""
    with app.test_client() as test_client:
        yield test_client

@pytest.fixture
def migrate_data():
    """Migrate (Create and insert) Postgres db data into sqlite db"""
    # PostgreSQL db connection Set up
    postgres_db_uri = config["development"]
    app.config.from_object(postgres_db_uri)
    postgres_engine = create_engine(postgres_db_uri)
    Session = sessionmaker(bind=postgres_engine)
    postgres_session = Session()

    # trajectory = Trajectory()
    # Query data from PostgreSQL tables
    taxis = postgres_session.query(Taxi).limit(5).all()
    trajectories = postgres_session.query(Trajectory).limit(10).all()

    # Then insert the above data (queried in Postgres) into sqlite db
    sqlite_db_uri = config["testing"]
    app.config.from_object(sqlite_db_uri)
    sqlite_engine = create_engine(sqlite_db_uri)
    Session = sessionmaker(bind=sqlite_engine)
    sqlite_session = Session()

    for taxi in taxis:
        new_taxi = Taxi(
            id=taxi.id,
            plate=taxi.plate
        )
        sqlite_session.add(new_taxi)

    for Trajectory in trajectories:
        new_trajectory = Trajectory(
            taxi_id=Trajectory.taxi_id,
            date=Trajectory.date,
            latitude=Trajectory.latitude,
            longitude=Trajectory.longitude
        )

    # Commit to save the changes
    sqlite_session.commit()

    # Close the sessions
    postgres_session.close()
    sqlite_session.close()

# @pytest.fixture
# def client():
#     """Client definition"""
#     # Configure Flask application in testing mode
#     testing_config = config["testing"]
#     print(testing_config)
#     app.config.from_object(testing_config)
#     # Configure a test client
#     with app.test_client() as test_client:
#         yield test_client

# @pytest.fixture
# def init_database(client):
#     """Initializing SQLite testing db"""
#     with app.app_context():
#         taxi1 = Taxi(id=7249, plate="CNCJ-2997")
#         taxi2 = Taxi(id=10133,	plate="PAOF-6727")
#         db.session.add(taxi1)
#         db.session.add(taxi2)
#         db.session.commit()
#         yield

# print(init_database)
# @pytest.fixture
# def client():
#     """Client definition"""
#     testing_confing = config["testing"]
#     app.config.from_object(testing_confing)
#     # Inserts using sqlalchemy api
#     # import taxi model
#     # from sqlalchemy import insert
#     # >>> from sqlalchemy import create_engine
#     # >>> engine = create_engine("sqlite://", echo=True)
#     # Base.metadata.create_all(engine)
#     # stmt = insert(Product).values(name='Printer', price=149.99)
#     # engine.connect().execute(stmt)
#     with app.test_client() as test_client:
#         yield test_client
