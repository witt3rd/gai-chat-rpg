# Message

Output of message data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**timestamp** | **object** |  | 
**campaign** | **object** |  | 
**sender** | **object** |  | 
**target** | **object** |  | [optional] 
**content** | **object** |  | 
**is_private** | **object** |  | 
**is_edited** | **object** |  | 

## Example

```python
from chat_rpg_client.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print Message.to_json()

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_form_dict = message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


