# CampaignUpdate

Update of campaign data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 

## Example

```python
from chat_rpg_client.models.campaign_update import CampaignUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignUpdate from a JSON string
campaign_update_instance = CampaignUpdate.from_json(json)
# print the JSON string representation of the object
print CampaignUpdate.to_json()

# convert the object into a dict
campaign_update_dict = campaign_update_instance.to_dict()
# create an instance of CampaignUpdate from a dict
campaign_update_form_dict = campaign_update.from_dict(campaign_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


