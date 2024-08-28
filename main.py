from fastapi import FastAPI
from app.src.router.snap_msgs import router

app = FastAPI()
app.include_router(router)

