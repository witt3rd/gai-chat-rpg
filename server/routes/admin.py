"""
System administration routes
"""
# # System # #

# # Packages # #
from fastapi import APIRouter
from loguru import logger

# # Project # #
from server.database import drop_db as drop_db

###

router = APIRouter()


@router.delete(
    "/db",
    status_code=200,
    description="Drop the database.",
    operation_id="drop_db",
)
async def delete_db() -> str:
    """
    Root endpoint for the API.
    """
    logger.info("Dropping database...")
    await drop_db()
    return "Database dropped!"
