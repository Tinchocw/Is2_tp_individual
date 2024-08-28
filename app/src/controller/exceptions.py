class BodyBadRequestException(Exception):
    def __init__(self, status_code, type, title, detail, instance):
        self.status_code = status_code
        self.type = type
        self.detail = detail
        self.title = title
        self.instance = instance

    def to_dic(self):
        return {
            "type": self.type,
            "title": self.title,
            "status": self.status_code,
            "detail": self.detail,
            "instance": self.instance
        }