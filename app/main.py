import os

import uvicorn
from fastapi import FastAPI
from src.router.router import Router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
router = Router().get_router()
app.include_router(router)

if __name__ == "__main__":
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))

    uvicorn.run(app, host=host, port=port)
