"""
This module contains the FastAPI application instance and its routes.
"""
# # System # #

# # Packages # #
from loguru import logger
from fastapi import FastAPI

# # Project # #
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
    return "Welcome to the generated realms of ChatRPG!"
