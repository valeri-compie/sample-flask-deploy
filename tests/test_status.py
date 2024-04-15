def test_request_example(client):
    response = client.get("/status")
    assert response.status_code == 200
