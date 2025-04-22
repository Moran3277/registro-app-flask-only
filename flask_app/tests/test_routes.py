def test_get_posts(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)

