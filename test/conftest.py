"""Client configuration"""
import pytest
from src.app import create_app
from src.config import config # db

app = create_app()

@pytest.fixture
def client():
    """Client definition"""
    testing_confing = config["testing"]
    app.config.from_object(testing_confing)
    # Inserts using sqlalchemy api
    # import taxi model
    # from sqlalchemy import insert
    # >>> from sqlalchemy import create_engine
    # >>> engine = create_engine("sqlite://", echo=True)
    # Base.metadata.create_all(engine)
    # stmt = insert(Product).values(name='Printer', price=149.99)
    # engine.connect().execute(stmt)
    with app.test_client() as test_client:
        yield test_client

# @pytest.fixture
# def client():
#     """Client definition"""
#     app.config['TESTING'] = True
#     with app.test_client() as test_client:
#         yield test_client
