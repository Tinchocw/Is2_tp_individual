from pydantic import BaseModel


class SnapMsgCreate(BaseModel):
    message: str


class SnapResponse(BaseModel):
    id: str
    message: str
