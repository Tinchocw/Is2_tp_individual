from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.src.controller.controller import Controller
from app.src.controller.exceptions import BodyBadRequestException

from app.src.schemas.schemas import SnapMsgCreate


class Router:
    def __init__(self):
        self.router = APIRouter()
        self.controller = Controller()
        self._setup_routes()

    '''Main protocol'''

    def get_router(self):
        return self.router

    '''private'''

    def _setup_routes(self):

        @self.router.post("/snap_msg/", status_code=Controller.http_201_created(), summary="Create a new snap")
        async def create_snap_msg(snap_msg: SnapMsgCreate):
            try:
                return self.controller.create_snap_msg(snap_msg)
            except BodyBadRequestException as e:
                return JSONResponse(
                    status_code=e.status_code,
                    content=e.to_dic()
                )
            except Exception as e:
                return JSONResponse(
                    status_code=Controller.http_500_internal_server_error(),
                    content={
                        "type": "about:blank",
                        "title": "Internal Server Error",
                        "status": Controller.http_500_internal_server_error(),
                        "detail": str(e),
                        "instance": "/snap_msg/"
                    }
                )

        @self.router.get("/snap_msg/", summary="A list of snaps")
        async def get_snap_messages():

            try:
                return self.controller.get_feed()
            except Exception as e:
                return JSONResponse(
                    status_code=Controller.http_500_internal_server_error(),
                    content={
                        "type": "about:blank",
                        "title": "Internal Server Error",
                        "status": Controller.http_500_internal_server_error(),
                        "detail": str(e),
                        "instance": "/snap_msg/"
                    }
                )
