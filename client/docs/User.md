# User

Output of user data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**username** | **object** |  | 
**name** | **object** |  | 
**email** | **object** |  | 
**password** | **object** |  | 
**avatar** | **object** |  | [optional] 
**is_admin** | **object** |  | 
**is_system** | **object** |  | 

## Example

```python
from chat_rpg_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


