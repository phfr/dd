from fastapi import WebSocket

from .logger import logger
from .websocket_manager import WebSocketManager

manager = WebSocketManager()


async def websocket_endpoint(websocket: WebSocket) -> None:
    await manager.connect(websocket)
    logger.info("WebSocket connection established.")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
            logger.info(f"Broadcasting message: {data}")
    except Exception as e:
        logger.error(f"Error in WebSocket connection: {e}")
        await manager.disconnect(websocket)
