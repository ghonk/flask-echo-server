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
    test_cases = [
        {"text": "", "expected_length": 0},
        {"text": "Hello, World!", "expected_length": 13},
        {"text": "  This string has spaces and special characters!@#$%^ ", "expected_length": 52}
    ]
    for case in test_cases:
        response = client.post('/strlen', json=case)
        assert response.status_code == 200
        assert response.get_json() == {"length": case["expected_length"]}

