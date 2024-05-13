"""Client configuration"""
import pytest
from sqlalchemy import create_engine, text
from src.app import create_app
from src.config import config

app = create_app()
# engine = None

@pytest.fixture
def client():
    """Client definition"""
    print("client")
    engine = None
    if not engine:
        engine = sqlite_connection()
    with app.test_client() as test_client:
        yield test_client

print("otra vez")
# @pytest.fixture
def sqlite_connection():
    """Create SQLite connection and insert data"""
    print("SQLite connection")
    # Configure app for testing
    app.config.from_object(config["testing"])
    # SQLite db connection set up
    sqlite_engine = create_engine(config["testing"].SQLALCHEMY_DATABASE_URI)
    
    # Queries
    with sqlite_engine.connect() as connection:
        # Query to create taxi table in sqlite db
        taxis = connection.execute(text("create table taxis (id serial primary key, plate varchar(9) not null);"))
        # Query to insert data into taxi table in sqlite db
        insert_data = connection.execute(taxis.insert(), [{"id":7249, "plate":"CNCJ-2997"},
            {"id":10133, "plate":"PAOF-6727"},
            {"id":6418, "plate":"GHGH-1458"}
        ])
        print(insert_data)
        # Close connection
        connection.close()
    return sqlite_engine
