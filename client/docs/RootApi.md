# chat_rpg_client.RootApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](RootApi.md#root_get) | **GET** / | Get Root


# **root_get**
> object root_get()

Get Root

Root endpoint for the API.

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
    api_instance = chat_rpg_client.RootApi(api_client)

    try:
        # Get Root
        api_response = api_instance.root_get()
        print("The response of RootApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootApi->root_get: %s\n" % e)
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

