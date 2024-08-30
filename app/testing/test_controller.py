import unittest
from app.src.controller.controller import Controller
from app.src.controller.exceptions import BodyBadRequestException

from app.src.schemas.schemas import SnapMsgCreate


class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.one_snap_message = SnapMsgCreate(message="Hello")
        self.another_snap_message = SnapMsgCreate(message="Goodbye")

    def test_01_create_snap_message_with_valid_body_request(self):
        snap_response = self.controller.create_snap_msg(self.one_snap_message)

        snap_response_expected = {
            "id": 1,
            "message": "Hello"
        }
        snap_response_body_expected = {"data": snap_response_expected}

        self.assertEqual(snap_response, snap_response_body_expected)

    def test_02_cannot_create_a_empty_snap_message(self):
        one_snap_msg = SnapMsgCreate(message="")

        with self.assertRaises(BodyBadRequestException) as context:
            self.controller.create_snap_msg(one_snap_msg)

        self.assertEqual(context.exception.status_code, Controller.http_400_bad_request())
        self.assertEqual(context.exception.type, "about:blank")
        self.assertEqual(context.exception.title, "Message Empty")
        self.assertEqual(context.exception.detail, "Message field cannot be empty")
        self.assertEqual(context.exception.instance, "/snap_msg/")

    def test_03_feed_format_is_correct_when_no_snaps_present(self):
        feed = self.controller.get_feed()

        expected_feed_response = {
            "data": []
        }

        self.assertEqual(feed, expected_feed_response)

    def test_04_feed_format_is_correct_with_one_snap(self):
        self.controller.create_snap_msg(self.one_snap_message)

        expected_feed_response = {
            "data": [
                {
                    "id": 1,
                    "message": self.one_snap_message.message
                }
            ]
        }

        self.assertEqual(self.controller.get_feed(), expected_feed_response)

    def test_05_feed_format_is_correct_with_multiple_snaps(self):
        self.controller.create_snap_msg(self.one_snap_message)
        self.controller.create_snap_msg(self.another_snap_message)

        expected_feed_response = {
            "data": [
                {
                    "id": 2,
                    "message": self.another_snap_message.message
                },
                {
                    "id": 1,
                    "message": self.one_snap_message.message
                }
            ]
        }

        self.assertEqual(self.controller.get_feed(), expected_feed_response)

    def test_06_can_not_create_280_character_lenght_snap_message(self):
        snap_msg = SnapMsgCreate(message="a" * 281)

        with self.assertRaises(BodyBadRequestException) as context:
            self.controller.create_snap_msg(snap_msg)

        self.assertEqual(context.exception.status_code, Controller.http_400_bad_request())
        self.assertEqual(context.exception.type, "about:blank")
        self.assertEqual(context.exception.title, "Message Too Long")
        self.assertEqual(context.exception.detail, "Message field cannot be longer than 280 characters")
        self.assertEqual(context.exception.instance, "/snap_msg/")


if __name__ == '__main__':
    unittest.main()
