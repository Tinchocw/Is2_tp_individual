from functools import reduce
from app.models.snap_msg import SnapMsg
import uuid


class Service:
    def __init__(self):
        self.feed = []


    '''Main protocol'''

    def create_snap_msg(self, snap_msg):
        msg = SnapMsg(str(uuid.uuid4()), snap_msg)
        self.feed.append(msg)
        return msg

    def get_feed(self):
        return self._order_feed()

    '''private'''

    def _order_feed(self):
        return reduce(lambda acc, x: [x] + acc, self.feed, [])
