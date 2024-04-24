# import pytest
# from app import app

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_get_taxis(client):
#     # Prueba básica para asegurarse de que la ruta de los taxis está disponible
#     response = client.get('/taxis')
#     assert response.status_code == 200

# def test_get_taxis_pagination(client):
#     # Prueba para verificar si la paginación funciona correctamente
#     response = client.get('/taxis?page=2&per_page=10')
#     data = response.get_json()
#     assert len(data) == 10  # Comprueba si devuelve 10 taxis por página