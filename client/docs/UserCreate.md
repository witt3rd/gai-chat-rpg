# UserCreate

New user data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** |  | 
**name** | **object** |  | 
**email** | **object** |  | 
**password** | **object** |  | 
**avatar** | **object** |  | [optional] 

## Example

```python
from chat_rpg_client.models.user_create import UserCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreate from a JSON string
user_create_instance = UserCreate.from_json(json)
# print the JSON string representation of the object
print UserCreate.to_json()

# convert the object into a dict
user_create_dict = user_create_instance.to_dict()
# create an instance of UserCreate from a dict
user_create_form_dict = user_create.from_dict(user_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


