import unittest
from app.src.service.service import Service


class ServiceTest(unittest.TestCase):

    def setUp(self):
        self.service = Service()
        self.msg_id = 1
        self.msg = 'Hello'

    def test_01_add_one_msg_to_feed(self):
        self.service.create_snap_msg(self.msg)
        feed = self.service.get_feed()
        self.assertTrue(len(feed) == 1)

    def test_02_add_more_than_one_msg_to_feed(self):
        self.service.create_snap_msg(self.msg)
        self.service.create_snap_msg(self.msg)
        feed = self.service.get_feed()
        self.assertTrue(len(feed) > 1)

    def test_03_create_two_msgs_with_different_id(self):
        one_msg = self.service.create_snap_msg(self.msg)
        another_msg = self.service.create_snap_msg(self.msg)

        self.assertNotEqual(one_msg.msg_id, another_msg.msg_id)

    def test_04_get_the_feed_in_the_chronological_order_inverted(self):
        one_msg = self.service.create_snap_msg(self.msg)
        another_msg = self.service.create_snap_msg(self.msg)

        snap_msgs = self.service.get_feed()
        expected_snap_msgs = [another_msg, one_msg]

        self.assertEqual(snap_msgs, expected_snap_msgs)


if __name__ == '__main__':
    unittest.main()
