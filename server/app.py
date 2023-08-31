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
    auth as auth_routes,
    users as user_routes,
)

###

# Setup FastAPI

app = FastAPI()
app.include_router(
    auth_routes.router,
    tags=["Authentication"],
    prefix="",
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
    tags=["root"],
)
async def read_root() -> dict[str, str]:
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the generated realms of ChatRPG!"}


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
