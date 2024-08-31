from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.exceptions.exceptions import EmptyMessageException, ObjectNotFoundException, MessageTooLongException
from app.schemas.responses import ResponseModel
from app.schemas.schemas import SnapMsgCreate
from app.schemas.status import Status
from app.src.controller.controller import Controller


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

        @self.router.post("/snaps/", status_code=Status.http_201_created(), summary="Create a new snap",
                          responses=ResponseModel.post_response_model())
        async def create_snap_msg(snap_msg: SnapMsgCreate):
            try:
                return self.controller.create_snap_msg(snap_msg)
            except EmptyMessageException as e:
                return JSONResponse(
                    status_code=e.status_code,
                    content=e.to_dic()
                )
            except MessageTooLongException as e:
                return JSONResponse(
                    status_code=e.status_code,
                    content=e.to_dic()
                )

            except Exception as e:
                return self._internal_server_error_response(e)

        @self.router.get("/snaps/", summary="A list of snaps", responses=ResponseModel.get_response_model())
        async def get_snap_messages():

            try:
                return self.controller.get_feed()
            except Exception as e:
                return self._internal_server_error_response(e)

        @self.router.get("/snaps/{snap_id}", summary="Retrieve a snap by ID",
                         responses=ResponseModel.get_by_id_response_model())
        async def get_snap_by_id(snap_id: str):
            try:
                return self.controller.get_snap_msg_by_id(snap_id)

            except ObjectNotFoundException as e:
                return JSONResponse(
                    status_code=e.status_code,
                    content=e.to_dic()
                )
            except Exception as e:
                return self._internal_server_error_response(e)

        @self.router.delete("/snaps/{snap_id}", status_code=Status.http_204_no_content(), summary="Delete a snap "
                                                                                                     "by ID",
                            responses=ResponseModel.delete_response_model())
        async def delete_snap_by_id(snap_id: str):
            try:
                return self.controller.delete_snap_by_id(snap_id)
            except ObjectNotFoundException as e:
                return JSONResponse(
                    status_code=e.status_code,
                    content=e.to_dic()
                )
            except Exception as e:
                return self._internal_server_error_response(e)

    def _internal_server_error_response(self, exception):
        return JSONResponse(
            status_code=Status.http_500_internal_server_error(),
            content={
                "type": "about:blank",
                "title": "Internal Server Error",
                "status": Status.http_500_internal_server_error(),
                "detail": f"{str(exception)}",
                "instance": "/snap_msg/"
            }
        )
