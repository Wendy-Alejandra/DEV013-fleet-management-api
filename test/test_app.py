"""endpoints unit tests"""
# taxis endpoint unit tests
def test_get_taxis(client):
    """Testing /taxis route is available"""
    response = client.get('/taxis')
    assert response.status_code == 200

def test_get_taxis_500_error(client):
    """Testing /taxis route error"""
    response = client.get('/taxis')
    assert not response.status_code == 500

def test_get_taxis_pagination(client):
    """Testing /taxis pagination is correctly working"""
    response = client.get('/taxis?page=2&per_page=10')
    data = response.get_json()
    assert len(data) == 10  # Checks if returns 10 taxis per page

# trajectories endpoint unit tests
def test_get_trajectories(client):
    """Testing /trajectories/taxi_id path is available"""
    response = client.get('/trajectories/6418?date=2008-02-02&page=10&per_page=10')
    assert response.status_code == 200

def test_get_trajectories_without_date(client):
    """Testing /trajectories/taxi_id without date"""
    response = client.get('/trajectories/6418?page=10&per_page=10')
    assert response.status_code == 400

def test_get_trajectories_invalid_format(client):
    """Testing /trajectories/taxi_id with invalid date format"""
    response = client.get('/trajectories/6418?date="2008-02-02"&page=10&per_page=10')
    assert response.status_code == 400

def test_get_trajectories_pagination(client):
    """Testing /trajectories/taxi_id pagination is correctly working"""
    response = client.get("/trajectories/6418?date=2008-02-02&page=10&per_page=10")
    data = response.get_json()
    assert len(data) == 10
