"""
User models
"""

# # System # #

# # Packages # #
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from pymongo import IndexModel, ASCENDING

# # Project # #

###


class CampaignDoc(Document):
    """
    Campaign database document
    """

    class Settings:
        collection = "campaigns"
        indexes = [
            IndexModel([("name", ASCENDING)], unique=True),
        ]

    name: str = Field(..., max_length=50)

    @classmethod
    async def create(
        cls,
        name: str,
    ) -> "CampaignDoc":
        """
        Creates a new campaign with the given username, email and password.
        """
        campaign_doc = cls(
            name=name,
        )
        await campaign_doc.insert()
        return campaign_doc


class CampaignCreate(BaseModel):
    """
    New campaign data
    """

    name: str


class CampaignUpdate(BaseModel):
    """
    Update of campaign data
    """

    name: str | None = None


class Campaign(BaseModel):
    """
    Output of campaign data
    """

    id: PydanticObjectId = Field(..., alias="_id")
    name: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}
