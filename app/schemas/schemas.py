from pydantic import BaseModel


class SnapMsgCreate(BaseModel):
    message: str

