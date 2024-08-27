from functools import reduce
from backend.models.snap_msg import SnapMsg


class Service:
    def __init__(self):
        self.feed = []
        self.id_counter = 0

    '''Main protocol'''

    def create_snap_msg(self, snap_msg):
        self.id_counter += 1
        msg = SnapMsg(self.id_counter, snap_msg)
        self.feed.append(msg)
        return msg

    def get_feed(self):
        return self._order_feed()

    '''private'''

    def _order_feed(self):
        return reduce(lambda acc, x: [x] + acc, self.feed, [])
