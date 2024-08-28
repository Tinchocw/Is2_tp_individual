from fastapi.testclient import TestClient
from app.main import app


class TestIntegration:

    def setup_method(self):
        self.client = TestClient(app)

    def test_01_create_valid_snap_msg(self):
        response = self.client.post("/snap_msg/", json={"message": "Hello"},)
        assert response.status_code == 201
        assert response.json() == {"data": {"id": 1, "message": "Hello"}}

    def test_02_get_snap_messages(self):

        response = self.client.get("/snap_msg/")
        assert response.status_code == 200
        assert response.json() == {"data": [{"id": 1, "message": "Hello"}]}

    def test_03_create_empty_snap_msg(self):
        response = self.client.post("/snap_msg/", json={"message": ""},)
        assert response.status_code == 400
        assert response.json() == {
            "type": "about:blank",
            "title": "Message Empty",
            "status": 400,
            "detail": "Message field cannot be empty",
            "instance": "/snap_msg/"
        }