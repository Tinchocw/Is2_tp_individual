import logging

from app.exceptions.exceptions import EmptyMessageException, MessageTooLongException
from app.src.service.service import Service

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self):
        self.service = Service()

    '''Main protocol'''

    def create_snap_msg(self, a_snap_msg):
        logger.info("Creating a new snap")

        self._check_empty_message(a_snap_msg.message)
        self._check_length_message(a_snap_msg.message)
        snap_msg = self.service.create_snap_msg(a_snap_msg.message)

        logger.info("Snap created")

        return self._create_snap_response(snap_msg)

    def get_feed(self):
        logger.info("Getting feed")
        feed = self.service.get_feed()
        return self._get_feed_body_response(feed)

    def get_snap_msg_by_id(self, snap_id):
        logger.info("Getting snap")
        snap_msg = self.service.get_snap_msg_by_id(snap_id)
        return self._create_snap_response(snap_msg)

    def delete_snap_by_id(self, snap_id):
        logger.info("Deleting snap")
        self.service.delete_snap_by_id(snap_id)

    '''private'''

    def _check_empty_message(self, a_snap_msg):
        if a_snap_msg == "":
            logger.info("Message field is empty")
            raise EmptyMessageException("Message field cannot be empty")

    def _check_length_message(self, a_snap_msg):
        if len(a_snap_msg) > 280:
            logger.info("Message field is too long")
            raise MessageTooLongException("Message field cannot be longer than 280 characters")

    def _create_snap_response(self, a_snap_msg):
        snap_response_expected = {
            "id": a_snap_msg.id,
            "message": a_snap_msg.msg
        }
        return {"data": snap_response_expected}

    def _get_feed_body_response(self, feed):
        return {"data": [{"id": snap.id, "message": snap.msg} for snap in feed]}
