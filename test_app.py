from app import app

client = app.test_client()

def test_add():

    response = client.get(
        "/add?a=10&b=20"
    )

    assert response.status_code == 200

    assert response.json["result"] == 30
