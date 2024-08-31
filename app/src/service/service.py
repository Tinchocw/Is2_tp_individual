from app.models.snap_msg import SnapMsg
import uuid
from app.src.controller.exceptions import ObjectNotFoundException
import logging

logger = logging.getLogger(__name__)

class Service:
    def __init__(self):
        self.feed = {}

    '''Main protocol'''

    def create_snap_msg(self, snap_msg):
        msg_id = str(uuid.uuid4())
        self.feed[msg_id] = snap_msg
        return SnapMsg(msg_id, snap_msg)

    def get_feed(self):
        return [SnapMsg(msg_id, msg) for msg_id, msg in reversed(self.feed.items())]

    def get_snap_msg_by_id(self, msg_id):
        self._check_id_exists(msg_id)
        snap_msg = self.feed.get(msg_id)
        return SnapMsg(msg_id, snap_msg)

    def delete_snap_by_id(self, msg_id):
        self._check_id_exists(msg_id)
        self.feed.pop(msg_id)

    '''private'''

    def _check_id_exists(self, msg_id):
        if msg_id not in self.feed:
            logger.info("Snap id not found")
            raise ObjectNotFoundException("Snap id not found")
