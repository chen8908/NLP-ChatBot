
from fastapi.testclient import TestClient
from run import app
from security import secret_token

client = TestClient(app)

def test_get_sentiment():
    respose = client.post(
        '/st/get_sentiment',
        headers={'x-token': secret_token},
        json={'message': '讚'}
    )

    assert respose.status_code == 200
    assert respose.json()['sentiment_keras_model'] == '正面'
