from app.src.service.service import Service
from app.src.controller.exceptions import BodyBadRequestException
import logging

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self):
        self.service = Service()

    @classmethod
    def http_200_ok(cls):
        return 200

    @classmethod
    def http_400_bad_request(cls):
        return 400

    @classmethod
    def http_201_created(cls):
        return 201

    @classmethod
    def http_404_not_found(cls):
        return 404

    @classmethod
    def http_500_internal_server_error(cls):
        return 500

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

    '''private'''

    def _check_empty_message(self, a_snap_msg):
        if a_snap_msg == "":
            logger.info("Message field is empty")

            raise BodyBadRequestException(
                status_code=Controller.http_400_bad_request(),
                type="about:blank",
                title="Message Empty",
                detail="Message field cannot be empty",
                instance="/snap_msg/"
            )

    def _check_length_message(self, a_snap_msg):
        if len(a_snap_msg) > 280:
            logger.info("Message field is too long")

            raise BodyBadRequestException(
                status_code=Controller.http_400_bad_request(),
                type="about:blank",
                title="Message Too Long",
                detail="Message field cannot be longer than 280 characters",
                instance="/snap_msg/"
            )

    def _create_snap_response(self, a_snap_msg):
        snap_response_expected = {
            "id": a_snap_msg.msg_id,
            "message": a_snap_msg.msg
        }
        return {"data": snap_response_expected}

    def _get_feed_body_response(self, feed):
        return {"data": [{"id": snap.msg_id, "message": snap.msg} for snap in feed]}
