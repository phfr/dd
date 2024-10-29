from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .logger import configure_logger
from .sum import router as sum_router
from .websocket import websocket_endpoint

app = FastAPI()

configure_logger()  # Configure the logger

app.include_router(sum_router)
app.mount("/static", StaticFiles(directory="logs"), name="static")

app.websocket("/ws")(websocket_endpoint)
