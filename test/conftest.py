"""Client configuration"""
import pytest
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Float, DateTime
from sqlalchemy.orm import sessionmaker
from src.app import create_app
from src.config import config

app = create_app()
# engine = None

@pytest.fixture
def client():
    """Client definition"""
    print("client")
    sqlite_connection()
    with app.test_client() as test_client:
        yield test_client

print("otra vez")
# @pytest.fixture(scope=session)
def sqlite_connection():
    """Create SQLite connection and insert data"""
    print("SQLite connection")
    # Configure app for testing
    app.config.from_object(config["testing"])
    # SQLite db connection set up
    sqlite_engine = create_engine(config["testing"].SQLALCHEMY_DATABASE_URI)

    # Define tables' schema
    metadata = MetaData()
    taxis_table = Table('taxis', metadata,
    Column('id', Integer, primary_key=True),
    Column('plate', String(9), nullable=False)
    )
    trajectories_table = Table('trajectories', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('taxi_id', Integer, ForeignKey('taxis.id')),
    Column('date', DateTime),
    Column('latitude', Float),
    Column('longitude', Float)
    )
    metadata.create_all(sqlite_engine)
    # Queries
    # Session = sessionmaker(bind=sqlite_engine)
    # session = Session()
    # Query to insert data into taxi table in sqlite db
    print("entra a engine.connect")
    # taxis_data = [
    #     {"id":7249, "plate":"CNCJ-2997"},
    #     {"id":6598, "plate":"FHLB-7962"}
    # ]
    taxis_table.insert().values(id=7249, plate="CNCJ-2997")
    taxis_table.insert().values(id=6598, plate="FHLB-7962")


    # trajectories_table.insert().values(taxi_id=6598, date="2008-02-02 13:40:26", latitude=116.29308, longitude=39.8804, id=2)
        
    # session.execute(taxis_table.insert(), [
    #     {"id":7249, "plate":"CNCJ-2997"},
    #     {"id":6598, "plate":"FHLB-7962"}
    # ])
    # (users.insert(), name='admin', email='admin@localhost')

    # session.execute(trajectories_table.insert(), [
    #     {"taxi_id": 6598, "date": "2008-02-02 13:40:26", "latitude": 116.29308, "longitude": 39.8804, "id":2},
    #     {"taxi_id": 6598, "date": "2008-02-02 13:45:26", "latitude": 116.29308, "longitude": 39.88038, "id":3},
    #     {"taxi_id": 6598, "date": "2008-02-02 13:50:26", "latitude": 116.29296, "longitude": 39.88037, "id":4},
    #     {"taxi_id": 7249, "date": "2008-02-03 13:36:06", "latitude": 116.29093, "longitude": 39.88667, "id":2838},
    #     {"taxi_id": 7249, "date": "2008-02-03 13:31:06", "latitude": 116.29109, "longitude": 39.88677, "id":2839},
    #     {"taxi_id": 7249, "date": "2008-02-03 13:41:06", "latitude": 116.29102, "longitude": 39.88675, "id":2840}
    # ])
    print("sale del bloque with")
    # session.commit()
    # session.close()
    return sqlite_engine

# import pytest
# from sqlalchemy import create_engine, text
# from src.app import create_app
# from src.config import config

# app = create_app()
# # engine = None

# @pytest.fixture
# def client():
#     """Client definition"""
#     print("client")
#     engine = None
#     if not engine:
#         engine = sqlite_connection()
#     with app.test_client() as test_client:
#         yield test_client

# print("otra vez")
# # @pytest.fixture
# def sqlite_connection():
#     """Create SQLite connection and insert data"""
#     print("SQLite connection")
#     # Configure app for testing
#     app.config.from_object(config["testing"])
#     # SQLite db connection set up
#     sqlite_engine = create_engine(config["testing"].SQLALCHEMY_DATABASE_URI)
    
#     # Queries
#     with sqlite_engine.connect() as connection:
#         # Query to create taxi table in sqlite db
#         taxis = connection.execute(text("create table taxis (id serial primary key, plate varchar(9) not null);"))
#         # Query to insert data into taxi table in sqlite db
#         insert_data = connection.execute(taxis.insert(), [{"id":7249, "plate":"CNCJ-2997"},
#             {"id":10133, "plate":"PAOF-6727"},
#             {"id":6418, "plate":"GHGH-1458"}
#         ])
#         print(insert_data)
#         # Close connection
#         connection.close()
#     return sqlite_engine