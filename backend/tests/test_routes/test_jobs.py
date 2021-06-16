# jobboard/tests/test_routes/test_jobs.py

import json


def test_create_job(client):
    data = {
        "title":"SDE 1 Yahoo",
        "company":"testhoo",
        "company_url":"https://www/fdj.com",
        "location":"USA,NY",
        "description":"Testing",
        "date_posted":"2022-07-20"
    }

    response = client.post("/jobs/create-job", json.dumps(data))
    assert response.status_code == 200
    