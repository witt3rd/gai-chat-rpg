"""
Persona API
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from beanie.exceptions import DocumentNotFound
from loguru import logger

# # Project # #
from server.config import get_config
from server.models import (
    PersonaDb,
    PersonaIn,
)

###


async def get_persona(
    persona_id: str,
) -> PersonaDb:
    """
    Get a persona by ID.
    """
    pid = PydanticObjectId(persona_id)
    persona_db = await PersonaDb.get(pid)
    if not persona_db:
        raise DocumentNotFound("Persona not found")
    return persona_db


async def add_persona(
    name: str,
    traits: str = "",
    story: str = "",
) -> PersonaDb:
    """
    Add a persona.
    """
    persona_db = PersonaDb(
        name=name,
        traits=traits,
        story=story,
    )
    await persona_db.insert()
    return persona_db


async def update_persona(
    persona_id: str,
    persona_update: PersonaIn,
) -> PersonaDb:
    """
    Update a persona by ID.
    """
    persona_db = await get_persona(persona_id)
    req = {k: v for k, v in persona_update.model_dump().items() if v is not None}
    update_query = {"$set": dict(req.items())}
    await persona_db.update(update_query)
    return persona_db


async def get_personas(
    skip: int = 0,
    limit: int = 100,
) -> list[PersonaDb]:
    """
    Get all personas.
    """
    personas_db = await PersonaDb.find(
        skip=skip,
        limit=limit,
    ).to_list()
    return personas_db


async def get_narrator_persona() -> PersonaDb:
    """
    Get the narrator persona.
    """
    narrator_db = await PersonaDb.find_one(PersonaDb.name == get_config().narrator)
    if not narrator_db:
        logger.info("Adding narrator persona...")
        narrator_db = PersonaDb(
            name=get_config().narrator,
            traits="",
            story="",
        )
        await narrator_db.insert()
    return narrator_db


async def analyze_persona(
    chat_id: str,
    persona_name: str,
) -> str:
    # chat_out = await get_chat(chat_id)
    # transcript = _get_transcript_from_chat(chat_out)
    # lower_persona_name = persona_name.strip().lower()
    # personas = [p for p in chat_out.personas if p.name.lower() == lower_persona_name]
    # if not personas:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid persona name"
    #     )
    # persona = personas[0]
    # analysis = ai_analyze_persona(
    #     transcript,
    #     persona.name,
    #     persona.story,
    # )
    # persona.traits = analysis
    # await persona.save()
    # return analysis
    pass
