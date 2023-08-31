# # System # #

# # Packages # #
from beanie import Document
from pydantic import BaseModel, Field

# # Project # #

###

# Define models


class PersonaDb(Document):
    """
    Persona suitable for the db.
    """

    name: str
    traits: str = Field(default_factory=str)
    story: str = Field(default_factory=str)

    class Settings:
        name = "persona"
        indexes = ["name"]


class PersonaIn(BaseModel):
    """
    Persona suitable for input.
    """

    name: str | None = None
    traits: str | None = None
    story: str | None = None


class PersonaOut(BaseModel):
    """
    Persona suitable for output.
    """

    name: str
    traits: str
    story: str
