import json
import pytest



from app.schemas.push_notification import PushNotificationSchema


def test_create_invalid_push_data(test_client, monkeypatch):
    test_request_payload = {
        "title": "test notification",
        "body": "test body"
    }

    test_response_payload = {"status": "in progress"}

    def mock_push_notification(notification: PushNotificationSchema):
        
        if notification.title and notification.body:
            return test_response_payload

    monkeypatch.setattr(
        "app.api.api_v1.endpoints.push_notification.push_notifications_to_users", mock_push_notification)

    response = test_client.post("/trigger-push-notifications", data=json.dumps(test_request_payload))
    assert response.status_code == 200
    assert response.json() == test_response_payload
