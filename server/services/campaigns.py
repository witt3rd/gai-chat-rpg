"""
Campaign services
"""
# # System # #

# # Packages # #
from beanie import PydanticObjectId
from loguru import logger

# # Project # #
from server.models import (
    campaign as campaign_models,
)


###


async def create_campaign(
    campaign_create: campaign_models.CampaignCreate,
) -> campaign_models.CampaignDoc:
    """
    Creates a new campaign with the given campaignname, email and password
    """
    doc_data = campaign_create.dict()
    campaign_doc = await campaign_models.CampaignDoc.create(**doc_data)
    logger.info(f"Created campaign {campaign_doc.name} ({campaign_doc.id})")
    return campaign_doc


async def all_campaigns() -> list[campaign_models.CampaignDoc]:
    """
    Get all campaigns
    """
    campaigns = campaign_models.CampaignDoc.all()
    return await campaigns.to_list()


async def update_campaign(
    id: PydanticObjectId,
    campaign: campaign_models.CampaignUpdate,
) -> campaign_models.CampaignDoc:
    """
    Updates a campaign with the given campaignname, email and password
    """
    campaign_doc = await campaign_models.CampaignDoc.get(id)
    if campaign_doc is None:
        raise ValueError(f"Campaign with id {id} does not exist")
    await campaign_doc.set(campaign.dict())
    logger.info(f"Updated campaign: {campaign_doc})")
    return campaign_doc


async def delete_campaign(
    id: PydanticObjectId,
) -> campaign_models.CampaignDoc:
    """
    Deletes a campaign
    """
    campaign_doc = await campaign_models.CampaignDoc.get(id)
    if campaign_doc is None:
        raise ValueError(f"Campaign with id {id} does not exist")
    await campaign_doc.delete()
    logger.info(f"Deleted campaign: {campaign_doc})")
    return campaign_doc
