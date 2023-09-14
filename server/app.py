"""
This module contains the FastAPI application and the websocket server
"""
# # System # #
import asyncio
import os
from typing import NoReturn

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


# Setup FastAPI

app = FastAPI()

# Routes

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

# App state

app.state.sockets = set()

###

#
# Websockets
#
import datetime
import random


async def register_socket(websocket) -> None:
    logger.info(f"Registering socket: {websocket}")
    app.state.sockets.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        app.state.sockets.remove(websocket)


async def show_time() -> NoReturn:
    while True:
        message = datetime.datetime.utcnow().isoformat() + "Z"
        websockets.broadcast(app.state.sockets, message)
        await asyncio.sleep(random.random() * 2 + 1)


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
async def socket_server() -> None:
    """
    Runs the websockets server.
    """
    logger.info(
        "Starting websockets server: ws://{host}:{port}",
        host=get_config().socket_host,
        port=get_config().socket_port,
    )
    async with websockets.serve(
        register_socket,
        get_config().socket_host,
        get_config().socket_port,
    ):
        await show_time()


if __name__ == "__main__":
    # Get the event loop and run the websockets server and FastAPI application
    loop = asyncio.get_event_loop()

    # Run the websockets server
    socket_server_task = loop.create_task(
        coro=socket_server(),
    )

    # Configure the FastAPI application
    watch_dir = os.path.dirname(__file__)
    config = Config(
        app="server.app:app",
        host=get_config().host,
        port=get_config().port,
        reload=True,
        reload_dirs=[str(watch_dir)],
    )

    # Run the FastAPI application
    server = Server(config)
    loop.run_until_complete(server.serve())

    # Cancel the websockets server
    socket_server_task.cancel()
    try:
        loop.run_until_complete(socket_server_task)
    except asyncio.CancelledError:
        pass

    # Shutdown the FastAPI application
    loop.run_until_complete(server.shutdown())

    # Close the event loop
    loop.close()
