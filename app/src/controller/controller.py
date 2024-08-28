from app.src.service.service import Service
from app.src.controller.exceptions import BodyBadRequestException


class Controller:
    def __init__(self):
        self.service = Service()

    '''Main protocol'''

    def create_snap_msg(self, a_snap_msg):
        self._check_empty_message(a_snap_msg.message)
        snap_msg = self.service.create_snap_msg(a_snap_msg.message)

        return self._create_snap_response(snap_msg)

    def get_feed(self):
        feed = self.service.get_feed()
        return self._get_feed_body_response(feed)

    '''private'''

    def _check_empty_message(self, a_snap_msg):
        if a_snap_msg == "":
            raise BodyBadRequestException(
                status_code=400,
                type="about:blank",
                title="Message Empty",
                detail="Message field cannot be empty",
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
