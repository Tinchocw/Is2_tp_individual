import unittest
from app.src.controller.controller import Controller
from app.schemas.status import Status
from app.exceptions.exceptions import EmptyMessageException, MessageTooLongException, ObjectNotFoundException
from unittest.mock import patch
from uuid import UUID

from app.schemas.schemas import SnapMsgCreate


class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.one_snap_message = SnapMsgCreate(message="Hello")
        self.another_snap_message = SnapMsgCreate(message="Goodbye")

    @patch('uuid.uuid4', return_value=UUID("12345678123456781234567812345678"))
    def test_01_create_snap_message_with_valid_body_request(self, mock_uuid):
        snap_response = self.controller.create_snap_msg(self.one_snap_message)

        snap_response_expected = {
            "id": str(mock_uuid.return_value),
            "message": "Hello"
        }
        snap_response_body_expected = {"data": snap_response_expected}

        self.assertEqual(snap_response, snap_response_body_expected)

    def test_02_cannot_create_a_empty_snap_message(self):
        one_snap_msg = SnapMsgCreate(message="")

        with self.assertRaises(EmptyMessageException) as context:
            self.controller.create_snap_msg(one_snap_msg)

        self.assertEqual(context.exception.status_code, Status.http_400_bad_request())
        self.assertEqual(context.exception.type, "about:blank")
        self.assertEqual(context.exception.title, "Message Empty")
        self.assertEqual(context.exception.detail, "Message field cannot be empty")
        self.assertEqual(context.exception.instance, "/snaps/")

    def test_03_feed_format_is_correct_when_no_snaps_present(self):
        feed = self.controller.get_feed()

        expected_feed_response = {
            "data": []
        }

        self.assertEqual(feed, expected_feed_response)

    @patch('uuid.uuid4', return_value=UUID("12345678123456781234567812345678"))
    def test_04_feed_format_is_correct_with_one_snap(self, mock_uuid):
        self.controller.create_snap_msg(self.one_snap_message)

        expected_feed_response = {
            "data": [
                {
                    "id": str(mock_uuid.return_value),
                    "message": self.one_snap_message.message
                }
            ]
        }

        self.assertEqual(self.controller.get_feed(), expected_feed_response)

    @patch('uuid.uuid4',
           side_effect=[UUID("12345678123456781234567812345678"), UUID("87654321876543218765432187654321")])
    def test_05_feed_format_is_correct_with_multiple_snaps(self, mock_uuid):
        self.controller.create_snap_msg(self.one_snap_message)
        self.controller.create_snap_msg(self.another_snap_message)

        expected_feed_response = {
            "data": [
                {
                    "id": str(UUID("87654321876543218765432187654321")),
                    "message": self.another_snap_message.message
                },
                {
                    "id": str(UUID("12345678123456781234567812345678")),
                    "message": self.one_snap_message.message
                }
            ]
        }

        self.assertEqual(self.controller.get_feed(), expected_feed_response)

    def test_06_can_not_create_280_character_lenght_snap_message(self):
        snap_msg = SnapMsgCreate(message="a" * 281)

        with self.assertRaises(MessageTooLongException) as context:
            self.controller.create_snap_msg(snap_msg)

        self.assertEqual(context.exception.status_code, Status.http_400_bad_request())
        self.assertEqual(context.exception.type, "about:blank")
        self.assertEqual(context.exception.title, "Message Too Long")
        self.assertEqual(context.exception.detail, "Message field cannot be longer than 280 characters")
        self.assertEqual(context.exception.instance, "/snaps/")

    def test_07_can_not_get_a_snap_that_does_not_exist(self):
        with self.assertRaises(ObjectNotFoundException) as context:
            self.controller.get_snap_msg_by_id(UUID("12345678123456781234567812345678"))

        self.assertEqual(context.exception.status_code, Status.http_404_not_found())
        self.assertEqual(context.exception.type, "about:blank")
        self.assertEqual(context.exception.title, "Snap not found")
        self.assertEqual(context.exception.detail, "Snap id not found")
        self.assertEqual(context.exception.instance, "/snaps/")

    def test_08_can_not_delete_a_snap_that_does_not_exist(self):
        with self.assertRaises(ObjectNotFoundException) as context:
            self.controller.delete_snap_by_id(UUID("12345678123456781234567812345678"))

        self.assertEqual(context.exception.status_code, Status.http_404_not_found())
        self.assertEqual(context.exception.type, "about:blank")
        self.assertEqual(context.exception.title, "Snap not found")
        self.assertEqual(context.exception.detail, "Snap id not found")
        self.assertEqual(context.exception.instance, "/snaps/")


if __name__ == '__main__':
    unittest.main()
