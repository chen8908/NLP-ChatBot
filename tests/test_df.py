
from fastapi.testclient import TestClient
from run import app
from security import secret_token

client = TestClient(app)

def test_get_df():
    response = client.post(
        '/df/get_df',
        headers={'x-token': secret_token},
        json={'message': '你好'}
    )

    assert response.status_code == 200
    assert response.json()['intent'] == 'Default Welcome Intent'
