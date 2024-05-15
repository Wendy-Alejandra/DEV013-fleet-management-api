"""endpoints unit tests"""
# import datetime
# taxis endpoint unit tests
def test_get_taxis(client):
    """Testing /taxis route is available"""
    response = client.get('/taxis')
    data = response.get_json()
    print(data)
    assert response.status_code == 200

def test_get_taxis_500_error(client):
    """Testing /taxis route error"""
    response = client.get('/taxis')
    assert not response.status_code == 500

def test_get_taxis_pagination(client):
    """Testing /taxis pagination is correctly working"""
    response = client.get('/taxis?page=1&per_page=2')
    data = response.get_json()
    print(data)
    assert len(data) == 2  # Checks if returns 2 taxis per page

# trajectories endpoint unit tests
def test_get_trajectories(client):
    """Testing /trajectories/taxi_id path is available"""
    response = client.get('/trajectories/6598?date=2008-02-02&page=1&per_page=2')
    assert response.status_code == 200


def test_get_trajectories_without_date_and_taxi(client):
    """Testing /trajectories/taxi_id without date"""
    response = client.get('/trajectories')
    assert response.status_code == 404

    response = client.get('/trajectories?page=1&per_page=2')
    assert response.status_code == 404

    response = client.get('/trajectories/6598?page=1&per_page=2')
    assert response.status_code == 400

    response = client.get('/trajectories/?date=2008-02-02&page=1&per_page=2')
    assert response.status_code == 404

def test_get_trajectories_invalid_format(client):
    """Testing /trajectories/taxi_id with invalid date format"""
    response = client.get('/trajectories/6598?date="2008-02-02"&page=1&per_page=2')
    assert response.status_code == 400

    response = client.get('/trajectories/6598?date=2008/02/02&page=1&per_page=2')
    assert response.status_code == 400


def test_get_trajectories_pagination(client):
    """Testing /trajectories/taxi_id pagination is correctly working"""
    response = client.get("/trajectories/6598?date=2008-02-02&page=1&per_page=2")
    data = response.get_json()
    assert len(data) == 2

# def test_get_trajectories_date_str(client):
#     response = client.get("/trajectories/6418?date=2008-02-02&page=10&per_page=10")
#     assert '2008-02-02' in response

# def test_trajectories_data_limit(migrate_data):
#     expected_value = [{"taxi_id": 6598, "date":	datetime.datetime(2008, 2, 2, 13, 40, 26), "latitude": 116.29308, "longitude": 39.8804, "id": 1},
#                         {"taxi_id": 6598, "date":	datetime.datetime(2008, 2, 2, 13, 40, 26), "latitude": 116.29308, "longitude": 39.8804, "id": 2},
#                         {"taxi_id": 6598, "date":	datetime.datetime(2008, 2, 2, 13, 45, 26), "latitude": 116.29308, "longitude": 39.88038, "id": 3},
#                         {"taxi_id": 6598, "date":	datetime.datetime(2008, 2, 2, 13, 50, 26), "latitude": 116.29296, "longitude": 39.88037, "id": 4},
#                         {"taxi_id": 6598, "date":	datetime.datetime(2008, 2, 2, 13, 55, 26), "latitude": 116.29301, "longitude": 39.88031, "id": 5},
#     ]
#     assert get_trajectories(migrate_data) == expected_value
