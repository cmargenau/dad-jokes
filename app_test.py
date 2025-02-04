import pytest, json, random
from app import app

app.json.sort_keys = False


# Fixtures in Pytest solve some of the problems of code duplication and boilerplate.
# They help you define reusable setup or teardown code that can be used across multiple tests.
# Instead of duplicating the same setup in every test, a fixture can be defined once and used in multiple tests.
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_one_joke(client):
    response = client.get('/')
    assert response.status_code == 200
    jokes = json.loads(response.data)
    assert len(jokes) == 1
    joke = jokes[0]
    assert 'question' in joke
    assert joke["question"] != "" and joke["question"] is not None
    assert 'answer' in joke
    assert joke["answer"] != "" and joke["answer"] is not None
    print("\n" + str(joke))


def test_random_number_of_jokes(client):
    # generate a random number between 1 and 10
    random_num = random.randint(1, 10)
    print("\njoke random number = " + str(random_num))

    response = client.get('/jokes/' + str(random_num))
    # confirm success response status
    assert response.status_code == 200

    jokes = json.loads(response.data)
    # confirm number of returned dicts matches request
    assert len(jokes) == random_num
    # confirm expected contents of q+a
    for joke in jokes:
        print(joke)
        assert 'question' in joke
        assert joke["question"] != "" and joke["question"] is not None
        assert 'answer' in joke
        assert joke["answer"] != "" and joke["answer"] is not None


def test_all_jokes(client):
    response = client.get('/jokes')
    assert response.status_code == 200
    jokes = json.loads(response.data)
    print("\njoke total number = " + str(len(jokes)))
    for joke in jokes:
        print(joke)
        assert 'question' in joke
        assert joke["question"] != "" and joke["question"] is not None
        assert 'answer' in joke
        assert joke["answer"] != "" and joke["answer"] is not None

