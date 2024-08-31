import os
import logging
import uvicorn
from fastapi import FastAPI
from app.src.router.router import Router
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                    ])

logging.info("Application started")

app = FastAPI()
router = Router().get_router()
app.include_router(router)

if __name__ == "__main__":
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))

    uvicorn.run(app, host=host, port=port)
