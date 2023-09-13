# MessageUpdate

Update of message data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | **object** |  | [optional] 
**sender** | **object** |  | [optional] 
**target** | **object** |  | [optional] 
**content** | **object** |  | [optional] 
**is_private** | **object** |  | [optional] 

## Example

```python
from chat_rpg_client.models.message_update import MessageUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MessageUpdate from a JSON string
message_update_instance = MessageUpdate.from_json(json)
# print the JSON string representation of the object
print MessageUpdate.to_json()

# convert the object into a dict
message_update_dict = message_update_instance.to_dict()
# create an instance of MessageUpdate from a dict
message_update_form_dict = message_update.from_dict(message_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


