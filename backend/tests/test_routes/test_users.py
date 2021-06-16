# jobboard/backend/tests/test_routes/test_users.py

import json


def test_create_user(client):
    data = {
        "username":"testuser",
        "email":"abc1@test.com",
        "password":"abc12345",
        }

    response = client.post("/users/",json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "abc1@test.com"
    assert response.json()["is_active"] == True
