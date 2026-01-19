import pytest
import sys
import os

# Add backend directory to path so we can import run
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard_endpoint(client):
    rv = client.get('/api/dashboard')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert 'user' in json_data
    assert json_data['user']['name'] == 'Alex Johnson'

def test_index_serving(client):
    rv = client.get('/')
    assert rv.status_code == 200
    # Check for some content that is expected in index.html
    assert b'GetReadyAi' in rv.data
