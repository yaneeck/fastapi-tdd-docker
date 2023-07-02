def test_ping(test_app):
    # Given
    # test_app

    # When

    # Then
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "ping": "pong",
        "testing": True,
    }
