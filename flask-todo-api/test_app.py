import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_todos_empty(client):
    rv = client.get('/todos')
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_add_todo(client):
    rv = client.post('/todos', json={'task': 'Test', 'done': False})
    assert rv.status_code == 201
    assert rv.get_json()['task'] == 'Test'

def test_update_todo(client):
    client.post('/todos', json={'task': 'Test', 'done': False})
    rv = client.put('/todos/0', json={'task': 'Updated', 'done': True})
    assert rv.status_code == 200
    assert rv.get_json()['task'] == 'Updated'

def test_delete_todo(client):
    client.post('/todos', json={'task': 'Test', 'done': False})
    rv = client.delete('/todos/0')
    assert rv.status_code == 200
    assert rv.get_json()['result'] is True