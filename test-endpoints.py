import requests
import json

BASE_URL = 'http://localhost:5000/v1/tasks'

def test_create_task():
    r = requests.post(BASE_URL, json={"title": "My First Task"})
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1

def test_list_all_tasks():
    r = requests.get(BASE_URL)
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) == 1
    assert isinstance(r.json()["tasks"][0]["id"], int)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 3

def test_get_task():
    r = requests.get(f'{BASE_URL}/1')
    assert isinstance(r.json(), dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 3

def test_update_task():
    r = requests.put(f'{BASE_URL}/1', json={"title": "My 1st Task", "is_completed": True})
    assert not r.content

def test_delete_task():
    r = requests.delete(f'{BASE_URL}/1')
    assert not r.content
