from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_create_movie_end_to_end(test_app: FlaskClient):
    client = app.test_client()
    response = test_app.get('/movies/new')
    response_data = response.data.decode("utf-8")
    assert response.status_code == 200
    assert '<h1 class="mb-5">Create Movie Rating</h1>' in response_data
    assert '<label for="title" class="form-label">Title:</label>' in response_data
    assert '<label for="director" class="form-label">Director:</label>' in response_data
    assert '<label for="rating" class="form-label">Rating:</label>' in response_data
    assert '<button type="submit" class="btn btn-primary">Create Movie</button>' in response_data

