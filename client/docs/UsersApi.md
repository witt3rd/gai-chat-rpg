# chat_rpg_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users/ | Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{id} | Delete User
[**get_all_users**](UsersApi.md#get_all_users) | **GET** /users/ | All Users
[**update_user**](UsersApi.md#update_user) | **PATCH** /users/{id} | Update User


# **create_user**
> User create_user(user_create)

Create User

Create a new user

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.models.user import User
from chat_rpg_client.models.user_create import UserCreate
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
    user_create = chat_rpg_client.UserCreate() # UserCreate | 

    try:
        # Create User
        api_response = api_instance.create_user(user_create)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**User**](User.md)

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

# **delete_user**
> User delete_user(id)

Delete User

Delete a user

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.models.user import User
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
    id = None # object | 

    try:
        # Delete User
        api_response = api_instance.delete_user(id)
        print("The response of UsersApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> object get_all_users()

All Users

Get all users

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
        # All Users
        api_response = api_instance.get_all_users()
        print("The response of UsersApi->get_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_all_users: %s\n" % e)
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

# **update_user**
> User update_user(id, user_update)

Update User

Update a user

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.models.user import User
from chat_rpg_client.models.user_update import UserUpdate
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
    id = None # object | 
    user_update = chat_rpg_client.UserUpdate() # UserUpdate | 

    try:
        # Update User
        api_response = api_instance.update_user(id, user_update)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

