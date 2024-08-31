from app.schemas.status import Status


class BodyBadRequestException(Exception):
    def __init__(self, status_code, type, title, detail, instance):
        self.status_code = status_code
        self.type = type
        self.title = title
        self.detail = detail
        self.instance = instance

    def to_dic(self):
        return {
            "type": self.type,
            "title": self.title,
            "status": self.status_code,
            "detail": self.detail,
            "instance": self.instance
        }


class EmptyMessageException(BodyBadRequestException):
    def __init__(self, detail):
        super().__init__(
            status_code=Status.http_400_bad_request(),
            type="about:blank",
            title="Message Empty",
            detail=detail,
            instance="/snap_msg/"
        )


class ObjectNotFoundException(BodyBadRequestException):
    def __init__(self, detail):
        super().__init__(
            status_code=Status.http_404_not_found(),
            type="about:blank",
            title="Snap not found",
            detail=detail,
            instance="/snap_msg/"
        )


class MessageTooLongException(BodyBadRequestException):
    def __init__(self, detail):
        super().__init__(
            status_code=Status.http_400_bad_request(),
            type="about:blank",
            title="Message Too Long",
            detail=detail,
            instance="/snap_msg/"
        )
