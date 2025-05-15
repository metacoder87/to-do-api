import os
import json
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

PERSIST_FILE = "todos.json"

def setup_module(module):
    # Remove the persist file before tests
    if os.path.exists(PERSIST_FILE):
        os.remove(PERSIST_FILE)

def teardown_module(module):
    # Clean up after tests
    if os.path.exists(PERSIST_FILE):
        os.remove(PERSIST_FILE)

def test_todos_are_persisted(client):
    # Add a todo
    client.post('/todos', json={'task': 'Persisted', 'done': False})
    # Check that the file exists and contains the todo
    assert os.path.exists(PERSIST_FILE)
    with open(PERSIST_FILE, "r") as f:
        data = json.load(f)
    assert data[0]['task'] == 'Persisted'

def test_todos_are_loaded_on_startup(client):
    # Simulate a restart by writing a todo to the file
    todos = [{'task': 'Loaded', 'done': True}]
    with open(PERSIST_FILE, "w") as f:
        json.dump(todos, f)
    # Now, GET /todos should return the loaded todo
    rv = client.get('/todos')
    assert rv.status_code == 200
    assert rv.get_json()[0]['task'] == 'Loaded'