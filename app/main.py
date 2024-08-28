from fastapi import FastAPI
from app.src.router.router import Router

app = FastAPI()
router = Router().get_router()
app.include_router(router)

