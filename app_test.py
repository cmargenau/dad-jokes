import pytest, json
from app import app


# Fixtures in Pytest solve some of the problems of code duplication and boilerplate.
# They help you define reusable setup or teardown code that can be used across multiple tests.
# Instead of duplicating the same setup in every test, a fixture can be defined once and used in multiple tests.
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = json.loads(response.data)
    assert 'question' in json_data
    assert json_data["question"] != "" and json_data["question"] is not None
    assert 'answer' in json_data
    assert json_data["answer"] != "" and json_data["answer"] is not None

