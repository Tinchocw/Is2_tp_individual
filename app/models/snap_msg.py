class SnapMsg:
    def __init__(self, msg_id, msg):
        self.id = msg_id
        self.msg = msg

    def is_equal(self, a_snap_msg):
        return self.id == a_snap_msg.id and self.msg == a_snap_msg.msg
