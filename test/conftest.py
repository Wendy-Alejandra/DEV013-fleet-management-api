"""Client configuration"""
import pytest
from src.app import app

@pytest.fixture
def client():
    """Client definition"""
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

@pytest.fixture(scope="module")
def api_url():
    """Defines the URL of the service I want to test"""
    return "http://127.0.0.1:5000/"
