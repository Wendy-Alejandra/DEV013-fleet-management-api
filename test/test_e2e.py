"""End to end tests"""
# from src.config import config
from src.models.taxi_route import get_taxis
from src.app import create_app

app = create_app()

# e2e testing using test_request_context()
def test_service_response(client):
    """Making a GET request to the web service"""
    with app.test_request_context(
        "/taxis", query_string={"per_page": 10, "page": 3}
    ):
        response = get_taxis() # Call the endpoint /taxis function
        print(response.__doc__)
        assert response.status_code == 200 # Verifies response has an HTTP 200 (OK) status code

# "/trajectories/6598", query_string={"date":"2008-02-02", "page"=1, "per_page":2"}
# e2e testing using requests library
# import requests
# import pytest
# def test_service_response():
#     """Making a GET request to the web service"""
#     api_url = "http://127.0.0.1:5000/taxis"
#     try:
#         response = requests.get(api_url, timeout=5)
#         # Verifies the response has an HTTP 200 (OK) status code
#         assert response.status_code == 200
#     except requests.exceptions.Timeout:
#         # Si la solicitud excede el tiempo de espera, se lanzará un error de Timeout
#         pytest.fail("La solicitud excedió el tiempo de espera.")
#     except requests.exceptions.RequestException as e:
#         # Manejar otros errores de solicitud
#         pytest.fail(f"Error de solicitud: {e}")
