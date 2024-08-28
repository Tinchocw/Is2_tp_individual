from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.src.controller.controller import Controller, BodyBadRequestException
from app.src.schemas.schemas import SnapMsgCreate

router = APIRouter()
controller = Controller()


@router.post("/snap_msg/", status_code=201, summary="Create a new snap")
async def create_snap_msg(snap_msg: SnapMsgCreate):
    try:
        return controller.create_snap_msg(snap_msg)
    except BodyBadRequestException as e:
        return JSONResponse(
            status_code=e.status_code,
            content=e.to_dic()
        )


@router.get("/snap_msg/", summary="A list of snaps")
async def get_snap_messages():
    return controller.get_feed()
