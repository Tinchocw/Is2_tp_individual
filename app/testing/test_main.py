from fastapi.testclient import TestClient
from app.src.controller.controller import Controller
from app.main import app


class TestMain:

    def setup_method(self):
        self.client = TestClient(app)

    def test_01_create_valid_snap_msg(self):
        response = self.client.post("/snap_msg/", json={"message": "Hello"},)
        assert response.status_code == Controller.http_201_created()
        assert response.json() == {"data": {"id": 1, "message": "Hello"}}

    def test_02_get_snap_messages(self):

        response = self.client.get("/snap_msg/")
        assert response.status_code == Controller.http_200_ok()
        assert response.json() == {"data": [{"id": 1, "message": "Hello"}]}

    def test_03_create_empty_snap_msg(self):
        response = self.client.post("/snap_msg/", json={"message": ""},)
        assert response.status_code == Controller.http_400_bad_request()
        assert response.json() == {
            "type": "about:blank",
            "title": "Message Empty",
            "status": Controller.http_400_bad_request(),
            "detail": "Message field cannot be empty",
            "instance": "/snap_msg/"
        }