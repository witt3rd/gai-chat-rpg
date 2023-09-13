"""
Campaign administration routes
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, status

# # Project # #
from server.models import (
    campaign as campaign_models,
)
from server.services import (
    campaigns as campaign_services,
)

###

router = APIRouter()


@router.get(
    "/",
    response_model=list[campaign_models.Campaign],
    status_code=status.HTTP_200_OK,
    description="Get all campaigns",
    operation_id="get_all_campaigns",
)
async def all_campaigns() -> list[campaign_models.Campaign]:
    """
    Get all campaigns
    """
    campaigns = await campaign_services.all_campaigns()
    campaigns_out = [
        campaign_models.Campaign(**campaign.dict(by_alias=False))
        for campaign in campaigns
    ]
    return campaigns_out


@router.post(
    "/",
    response_model=campaign_models.Campaign,
    status_code=status.HTTP_201_CREATED,
    description="Create a new campaign",
    operation_id="create_campaign",
)
async def create_campaign(
    campaign: campaign_models.CampaignCreate,
) -> campaign_models.Campaign:
    """
    Create a new campaign
    """
    campaign_doc = await campaign_services.create_campaign(campaign)
    return campaign_models.Campaign(**campaign_doc.dict())


@router.patch(
    "/{id}",
    response_model=campaign_models.Campaign,
    status_code=status.HTTP_200_OK,
    description="Update a campaign",
    operation_id="update_campaign",
)
async def update_campaign(
    id: str,
    campaign: campaign_models.CampaignUpdate,
) -> campaign_models.Campaign:
    """
    Update a campaign
    """
    print(f"\n\nID: {id}\n{campaign}\n\n")
    try:
        campaign_id = PydanticObjectId(id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid campaign ID.",
        )
    campaign_doc = await campaign_services.update_campaign(
        id=campaign_id,
        campaign=campaign,
    )
    return campaign_models.Campaign(**campaign_doc.dict())


@router.delete(
    "/{id}",
    response_model=campaign_models.Campaign,
    status_code=status.HTTP_200_OK,
    description="Delete a campaign",
    operation_id="delete_campaign",
)
async def delete_campaign(
    id: str,
) -> campaign_models.Campaign:
    """
    Delete a campaign
    """
    try:
        campaign_id = PydanticObjectId(id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid campaign ID.",
        )
    campaign_doc = await campaign_services.delete_campaign(
        id=campaign_id,
    )
    return campaign_models.Campaign(**campaign_doc.dict())
