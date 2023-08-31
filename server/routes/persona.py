"""
Persona API
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, status
from loguru import logger

# # Project # #
from server.config import get_config
from server.models import (
    PersonaDb,
    PersonaIn,
    PersonaOut,
)
from server.services import persona as persona_service

###

router = APIRouter()


@router.post(
    "/",
    response_model=PersonaOut,
)
async def add_persona(
    name: str,
    traits: str = "",
    story: str = "",
) -> PersonaOut:
    return await persona_service.add_persona(
        name,
        traits,
        story,
    )


@router.patch(
    "/{persona_id}",
    response_model=PersonaOut,
    responses={
        404: {"description": "Persona not found"},
        400: {"description": "Invalid persona ID"},
    },
)
async def update_persona(
    persona_id: str,
    persona_update: PersonaIn,
) -> PersonaOut:
    return await persona_service.update_persona(
        persona_id,
        persona_update,
    )


@router.get(
    "/",
    response_model=list[PersonaOut],
)
async def get_personas(
    skip: int = 0,
    limit: int = 100,
) -> list[PersonaOut]:
    return await persona_service.get_personas(
        skip,
        limit,
    )


@router.get(
    "/{persona_id}",
    response_model=PersonaOut,
    responses={
        404: {"description": "Persona not found"},
        400: {"description": "Invalid persona ID"},
    },
)
async def get_persona(
    persona_id: str,
) -> PersonaOut:
    return await persona_service.get_persona(persona_id)


@router.get(
    "/narrator",
)
async def get_narrator_persona() -> PersonaOut:
    return await persona_service.get_narrator_persona()


@router.post(
    "/{persona_id}/analyze",
    response_model=str,
    responses={
        404: {"description": "Persona not found"},
        400: {"description": "Invalid persona ID"},
    },
)
async def analyze_persona(
    chat_id: str,
    persona_name: str,
) -> str:
    # TODO: Implement
    pass
