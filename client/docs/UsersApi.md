# chat_rpg_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_users_post**](UsersApi.md#user_users_post) | **POST** /users/ | Create User
[**users_users_get**](UsersApi.md#users_users_get) | **GET** /users/ | Get Users


# **user_users_post**
> UserOut user_users_post(user_signup)

Create User

Create a new user.

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.models.user_out import UserOut
from chat_rpg_client.models.user_signup import UserSignup
from chat_rpg_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = chat_rpg_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with chat_rpg_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chat_rpg_client.UsersApi(api_client)
    user_signup = chat_rpg_client.UserSignup() # UserSignup | 

    try:
        # Create User
        api_response = api_instance.user_users_post(user_signup)
        print("The response of UsersApi->user_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_users_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_signup** | [**UserSignup**](UserSignup.md)|  | 

### Return type

[**UserOut**](UserOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_users_get**
> object users_users_get()

Get Users

Get all users.

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = chat_rpg_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with chat_rpg_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chat_rpg_client.UsersApi(api_client)

    try:
        # Get Users
        api_response = api_instance.users_users_get()
        print("The response of UsersApi->users_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_users_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

