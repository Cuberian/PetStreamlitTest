import pytest
import json
from api import create_app


# обязательно для тестирования
@pytest.fixture()
def app():
    app = create_app()
    yield app


# обязательно для тестирования
@pytest.fixture()
def client(app):
    return app.test_client()


# проверка работы запроса на '/'
def test_home(client):
    response = client.get("/")
    assert response.data == b'Home'


# проверка работы запроса на '/get-user/123?extra=bub'
def test_get_user(client):
    response = client.get("/get-user/123?extra=bub")
    data = json.loads(response.data)
    assert data['extra'] == 'bub' and \
           data['name'] == 'John Doe'
