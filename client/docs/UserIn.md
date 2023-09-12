# UserIn

Update of user data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** |  | [optional] 
**name** | **object** |  | [optional] 
**email** | **object** |  | [optional] 
**password** | **object** |  | [optional] 

## Example

```python
from chat_rpg_client.models.user_in import UserIn

# TODO update the JSON string below
json = "{}"
# create an instance of UserIn from a JSON string
user_in_instance = UserIn.from_json(json)
# print the JSON string representation of the object
print UserIn.to_json()

# convert the object into a dict
user_in_dict = user_in_instance.to_dict()
# create an instance of UserIn from a dict
user_in_form_dict = user_in.from_dict(user_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


