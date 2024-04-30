"""End to end tests"""
import requests
import pytest
from .conftest import api_url

def test_service_response(api_url):
    """Making a GET request to the web service"""
    try:
        response = requests.get(api_url + "/endpoint", Timeout=5)
        # Verifies the response has an HTTP 200 (OK) status code
        assert response.status_code == 200
    except requests.exceptions.Timeout:
        # Si la solicitud excede el tiempo de espera, se lanzará un error de Timeout
        pytest.fail("La solicitud excedió el tiempo de espera.")
    except requests.exceptions.RequestException as e:
        # Manejar otros errores de solicitud
        pytest.fail(f"Error de solicitud: {e}")
