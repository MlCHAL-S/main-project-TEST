
def test_index(client):
    """ This should get 200_OK from the Index Page. """
    response = client.get('/')
    assert response.status_code == 200
