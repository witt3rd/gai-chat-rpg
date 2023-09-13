# UserOut

Output of user data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**username** | **object** |  | 
**name** | **object** |  | 
**email** | **object** |  | 
**password** | **object** |  | 
**is_admin** | **object** |  | 

## Example

```python
from chat_rpg_client.models.user_out import UserOut

# TODO update the JSON string below
json = "{}"
# create an instance of UserOut from a JSON string
user_out_instance = UserOut.from_json(json)
# print the JSON string representation of the object
print UserOut.to_json()

# convert the object into a dict
user_out_dict = user_out_instance.to_dict()
# create an instance of UserOut from a dict
user_out_form_dict = user_out.from_dict(user_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


