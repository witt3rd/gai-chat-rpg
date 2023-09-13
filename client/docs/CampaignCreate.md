# CampaignCreate

New campaign data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 

## Example

```python
from chat_rpg_client.models.campaign_create import CampaignCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignCreate from a JSON string
campaign_create_instance = CampaignCreate.from_json(json)
# print the JSON string representation of the object
print CampaignCreate.to_json()

# convert the object into a dict
campaign_create_dict = campaign_create_instance.to_dict()
# create an instance of CampaignCreate from a dict
campaign_create_form_dict = campaign_create.from_dict(campaign_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


