# chat_rpg_client.MessagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_message**](MessagesApi.md#delete_message) | **DELETE** /messages/{id} | Delete Message
[**send_message**](MessagesApi.md#send_message) | **POST** /messages/{campaign} | Send Message
[**update_message**](MessagesApi.md#update_message) | **PATCH** /messages/{id} | Update Message


# **delete_message**
> Message delete_message(id)

Delete Message

Delete a message

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.models.message import Message
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
    api_instance = chat_rpg_client.MessagesApi(api_client)
    id = None # object | 

    try:
        # Delete Message
        api_response = api_instance.delete_message(id)
        print("The response of MessagesApi->delete_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->delete_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Message**](Message.md)

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

# **send_message**
> Message send_message(campaign, message_create)

Send Message

Create a new message.

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.models.message import Message
from chat_rpg_client.models.message_create import MessageCreate
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
    api_instance = chat_rpg_client.MessagesApi(api_client)
    campaign = None # object | 
    message_create = chat_rpg_client.MessageCreate() # MessageCreate | 

    try:
        # Send Message
        api_response = api_instance.send_message(campaign, message_create)
        print("The response of MessagesApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**object**](.md)|  | 
 **message_create** | [**MessageCreate**](MessageCreate.md)|  | 

### Return type

[**Message**](Message.md)

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

# **update_message**
> Message update_message(id, message_update)

Update Message

Update a message.

### Example

```python
import time
import os
import chat_rpg_client
from chat_rpg_client.models.message import Message
from chat_rpg_client.models.message_update import MessageUpdate
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
    api_instance = chat_rpg_client.MessagesApi(api_client)
    id = None # object | 
    message_update = chat_rpg_client.MessageUpdate() # MessageUpdate | 

    try:
        # Update Message
        api_response = api_instance.update_message(id, message_update)
        print("The response of MessagesApi->update_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->update_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **message_update** | [**MessageUpdate**](MessageUpdate.md)|  | 

### Return type

[**Message**](Message.md)

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

