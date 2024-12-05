import pytest
from flask_echo_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_echo(client):
    response = client.post('/echo', json={"message": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"echo": {"message": "Hello, World!"}}


def test_strlen(client):
    response = client.post('/strlen', json={"string": "test"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 4}

def test_strlen_empty(client):
    response = client.post('/strlen', json={"string": ""})
    assert response.status_code == 200
    assert response.get_json() == {"length": 0}

def test_strlen_missing_key(client):
    response = client.post('/strlen', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Missing 'string' key"}

