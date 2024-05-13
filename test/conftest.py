"""Client configuration"""
import pytest
# from sqlalchemy import create_engine, text #MetaData
# from sqlalchemy.orm import sessionmaker
from src.app import create_app
from src.config import config
# from src.models.models import Taxi, Trajectory

app = create_app(config["testing"])

@pytest.fixture
def client():
    """Client definition"""
    with app.test_client() as test_client:
        yield test_client

# @pytest.fixture
# def sqlite_connection():
#     """Migrate (Create and insert) Postgres db data into sqlite db"""
#     # PostgreSQL db connection Set up
#     sqlite_db_uri = config["testing"]
#     app.config.from_object(sqlite_db_uri)
#     sqlite_engine = create_engine(sqlite_db_uri)
#     # metadata = MetaData(bind=sqlite_engine)
#     # Session = sessionmaker(bind=sqlite_engine)
#     # sqlite_session = Session()

#     with sqlite_engine.connect() as connection:
#         result = connection.execute(text("create table taxis (id serial primary key, plate varchar(9) not null);"))
#         print(result)
    # Query to create tables into sqlite db
    # metadata_obj = MetaData()
    # tables = metadata_obj.create_all(sqlite_engine)
    # trajectories = Trajectory.create(sqlite_engine)

    # Query to insert data into sqlite db

    # for taxi in taxis:
    #     new_taxi = Taxi(
    #         id=taxi.id,
    #         plate=taxi.plate
    #     )
    #     sqlite_session.add(new_taxi)

    # for Trajectory in trajectories:
    #     new_trajectory = Trajectory(
    #         taxi_id=Trajectory.taxi_id,
    #         date=Trajectory.date,
    #         latitude=Trajectory.latitude,
    #         longitude=Trajectory.longitude
    #     )

    # # Commit to save the changes
    # sqlite_session.commit()

    # # Close the sessions
    # sqlite_session.close()

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
