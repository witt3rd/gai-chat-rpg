# UserSignup

Model to handle data of signup request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** |  | 
**name** | **object** |  | 
**email** | **object** |  | 
**password** | **object** |  | 

## Example

```python
from chat_rpg_client.models.user_signup import UserSignup

# TODO update the JSON string below
json = "{}"
# create an instance of UserSignup from a JSON string
user_signup_instance = UserSignup.from_json(json)
# print the JSON string representation of the object
print UserSignup.to_json()

# convert the object into a dict
user_signup_dict = user_signup_instance.to_dict()
# create an instance of UserSignup from a dict
user_signup_form_dict = user_signup.from_dict(user_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


