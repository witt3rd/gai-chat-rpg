# MessageCreate

New message data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | **object** |  | 
**sender** | **object** |  | 
**target** | **object** |  | 
**content** | **object** |  | 

## Example

```python
from chat_rpg_client.models.message_create import MessageCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCreate from a JSON string
message_create_instance = MessageCreate.from_json(json)
# print the JSON string representation of the object
print MessageCreate.to_json()

# convert the object into a dict
message_create_dict = message_create_instance.to_dict()
# create an instance of MessageCreate from a dict
message_create_form_dict = message_create.from_dict(message_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


