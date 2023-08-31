"""
This module contains the FastAPI application instance and its routes.
"""
# # System # #

# # Packages # #
from loguru import logger
from fastapi import FastAPI

# # Project # #
from server.database import init_db, drop_db
from server.routes import (
    ChatRouter,
    PersonaRouter,
)

###

# Setup FastAPI

app = FastAPI()
app.include_router(
    ChatRouter,
    tags=["Chats"],
    prefix="/chats",
)
app.include_router(
    PersonaRouter,
    tags=["Personas"],
    prefix="/personas",
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
    tags=["root"],
)
async def read_root() -> dict[str, str]:
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Dittoverse API!"}


@app.post(
    "/admin/drop_db",
    tags=["admin"],
)
async def admin_drop_db() -> dict[str, str]:
    """
    Root endpoint for the API.
    """
    await drop_db()
    return {"message": "Database dropped!"}
