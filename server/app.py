"""
This module contains the FastAPI application instance and its routes.
"""
# # System # #
import asyncio
import os

# # Packages # #
from loguru import logger
from fastapi import FastAPI
from uvicorn import Config, Server
import websockets


# # Project # #
from server.config import get_config
from server.database import init_db
from server.routes import (
    admin as admin_routes,
    campaigns as campaign_routes,
    messages as message_routes,
    users as user_routes,
)

###

#
# Websockets
#


# create handler for each connection
async def handler(websocket, path) -> None:
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"
    await websocket.send(reply)


# Setup FastAPI

app = FastAPI()
app.include_router(
    admin_routes.router,
    tags=["Admin"],
    prefix="/admin",
)
app.include_router(
    campaign_routes.router,
    tags=["Campaigns"],
    prefix="/campaigns",
)
app.include_router(
    message_routes.router,
    tags=["Messages"],
    prefix="/messages",
)
app.include_router(
    user_routes.router,
    tags=["Users"],
    prefix="/users",
)

###

#
# Application Events
#


@app.on_event("startup")
async def on_startup() -> None:
    """
    Initializes the MongoDB database connection on application startup.
    """
    logger.info("Initializing MongoDB...")
    await init_db()


#
# API Endpoints
#


@app.get(
    "/",
    tags=["Root"],
    status_code=200,
    description="Root endpoint for the API.",
    operation_id="get_root",
)
async def get_root() -> str:
    """
    Root endpoint for the API.
    """
    return "Welcome to the generated realms of ChatRPG"


#
# Main
#


async def my_coroutine():
    # Run another async operation
    await asyncio.sleep(2)
    print("Coroutine finished")


if __name__ == "__main__":
    # Start the event loop
    start_server = websockets.serve(handler, "localhost", 9000)

    loop = asyncio.get_event_loop()

    loop.run_until_complete(start_server)
    # loop.run_forever()

    # Create a task for the coroutine
    task = loop.create_task(my_coroutine())

    # Start the FastAPI application
    watch_dir = os.path.dirname(__file__)
    config = Config(
        app="server.app:app",
        host=get_config().host,
        port=get_config().port,
        reload=True,
        reload_dirs=[str(watch_dir)],
    )

    # Run the event loop until the task is complete
    loop.run_until_complete(task)

    # Run the FastAPI application
    server = Server(config)
    loop.run_until_complete(server.serve())
    loop.run_until_complete(server.shutdown())
    loop.close()
