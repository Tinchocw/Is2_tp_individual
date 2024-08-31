from unittest.mock import patch
from uuid import UUID

from fastapi.testclient import TestClient
from app.schemas.status import Status
from app.main import app


class TestMain:

    def setup_method(self):
        self.client = TestClient(app)

    @patch('uuid.uuid4', return_value=UUID("12345678123456781234567812345678"))
    def test_01_create_valid_snap_msg(self, mock_uuid):
        response = self.client.post("/snap_msg/", json={"message": "Hello"}, )
        assert response.status_code == Status.http_201_created()
        assert response.json() == {"data": {"id": str(mock_uuid.return_value), "message": "Hello"}}

    @patch('uuid.uuid4', return_value=UUID("12345678123456781234567812345678"))
    def test_02_get_snap_messages(self, mock_uuid):
        response = self.client.get("/snap_msg/")
        assert response.status_code == Status.http_200_ok()
        assert response.json() == {"data": [{"id": str(mock_uuid.return_value), "message": "Hello"}]}

    def test_03_create_empty_snap_msg(self):
        response = self.client.post("/snap_msg/", json={"message": ""}, )
        assert response.status_code == Status.http_400_bad_request()
        assert response.json() == {
            "type": "about:blank",
            "title": "Message Empty",
            "status": Status.http_400_bad_request(),
            "detail": "Message field cannot be empty",
            "instance": "/snap_msg/"
        }

    def test_04_create_long_snap_msg(self):
        response = self.client.post("/snap_msg/", json={"message": "a" * 281}, )
        assert response.status_code == Status.http_400_bad_request()
        assert response.json() == {
            "type": "about:blank",
            "title": "Message Too Long",
            "status": Status.http_400_bad_request(),
            "detail": "Message field cannot be longer than 280 characters",
            "instance": "/snap_msg/"
        }

    def test_05_get_snap_message_by_id(self):
        response = self.client.get("/snap_msg/12345678-1234-5678-1234-567812345678")
        assert response.status_code == Status.http_200_ok()
        assert response.json() == {"data": {"id": "12345678-1234-5678-1234-567812345678", "message": "Hello"}}

    def test_06_get_snap_message_by_invalid_id(self):
        response = self.client.get("/snap_msg/12345678-1234-5678-1234-567812345679")
        assert response.status_code == Status.http_404_not_found()
        assert response.json() == {
            "type": "about:blank",
            "title": "Snap not found",
            "status": Status.http_404_not_found(),
            "detail": "Snap id not found",
            "instance": "/snap_msg/"
        }

    def test_07_delete_snap_message_by_id(self):
        response = self.client.delete("/snap_msg/12345678-1234-5678-1234-567812345678")
        assert response.status_code == Status.http_204_no_content()

    def test_08_delete_snap_message_by_invalid_id(self):
        response = self.client.delete("/snap_msg/12345678-1234-5678-1234-567812345679")
        assert response.status_code == Status.http_404_not_found()
        assert response.json() == {
            "type": "about:blank",
            "title": "Snap not found",
            "status": Status.http_404_not_found(),
            "detail": "Snap id not found",
            "instance": "/snap_msg/"
        }

