import unittest
from app.src.service.service import Service
from app.src.exceptions.exceptions import ObjectNotFoundException


class ServiceTest(unittest.TestCase):

    def setUp(self):
        self.service = Service()
        self.one_msg_id = 'e9aaff4e-8605-4a56-9f68-631540dcc5a8'
        self.one_msg = 'Hello'
        self.another_msg_id = 'e9aaff4e-8605-4a56-9f68-631540dcc5a9'
        self.another_msg = 'Goodbye'

    def test_01_add_one_msg_to_feed(self):
        self.service.create_snap_msg(self.one_msg)
        feed = self.service.get_feed()
        self.assertTrue(len(feed) == 1)

    def test_02_add_more_than_one_msg_to_feed(self):
        self.service.create_snap_msg(self.one_msg)
        self.service.create_snap_msg(self.one_msg)
        feed = self.service.get_feed()
        self.assertTrue(len(feed) > 1)

    def test_03_create_two_msgs_with_different_id(self):
        one_snap_msg = self.service.create_snap_msg(self.one_msg)
        another_snap_msg = self.service.create_snap_msg(self.one_msg)

        self.assertNotEqual(one_snap_msg.id, another_snap_msg.id)

    def test_04_get_the_feed_in_the_chronological_order_inverted(self):
        one_snap_msg = self.service.create_snap_msg(self.one_msg)
        another_snap_msg = self.service.create_snap_msg(self.one_msg)

        snap_msgs = self.service.get_feed()

        self.assertTrue(another_snap_msg.is_equal(snap_msgs[0]))
        self.assertTrue(one_snap_msg.is_equal(snap_msgs[1]))

    def test_05_get_a_snap_by_ip(self):
        snap_msg_expected = self.service.create_snap_msg(self.one_msg)

        self.assertTrue(self.service.get_snap_msg_by_id(snap_msg_expected.id).is_equal(snap_msg_expected))

    def test_06_get_snap_by_id_raises_error_if_not_found(self):
        self.service.create_snap_msg(self.one_msg)

        self.assertRaises(ObjectNotFoundException, self.service.get_snap_msg_by_id, self.another_msg_id )

    def test_07_delete_a_snap_by_id(self):
        snap_msg = self.service.create_snap_msg(self.one_msg)
        self.service.delete_snap_by_id(snap_msg.id)
        self.assertTrue(len(self.service.get_feed()) == 0)

    def test_08_can_not_delete_a_snap_that_does_not_exist(self):
        self.assertRaises(ObjectNotFoundException, self.service.delete_snap_by_id, self.another_msg_id)


if __name__ == '__main__':
    unittest.main()
