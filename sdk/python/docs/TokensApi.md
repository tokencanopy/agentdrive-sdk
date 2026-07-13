# agentdrive_sdk.TokensApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tokens_v0_tokens_get**](TokensApi.md#list_tokens_v0_tokens_get) | **GET** /v0/tokens | List your user-identity tokens
[**revoke_token_v0_tokens_token_id_revoke_post**](TokensApi.md#revoke_token_v0_tokens_token_id_revoke_post) | **POST** /v0/tokens/{token_id}/revoke | Revoke one of your user-identity tokens


# **list_tokens_v0_tokens_get**
> UserTokenList list_tokens_v0_tokens_get(cursor=cursor, limit=limit, authorization=authorization)

List your user-identity tokens

List the `ad_user_` tokens belonging to the authenticated user. Metadata only — the raw token is shown once at mint (web only) and is never returned here. Includes recently-revoked tokens (with `revoked_at` set) so the caller can audit them; newest first.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.user_token_list import UserTokenList
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.TokensApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List your user-identity tokens
        api_response = api_instance.list_tokens_v0_tokens_get(cursor=cursor, limit=limit, authorization=authorization)
        print("The response of TokensApi->list_tokens_v0_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->list_tokens_v0_tokens_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**UserTokenList**](UserTokenList.md)

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

# **revoke_token_v0_tokens_token_id_revoke_post**
> UserTokenOut revoke_token_v0_tokens_token_id_revoke_post(token_id, authorization=authorization)

Revoke one of your user-identity tokens

Revoke a single `ad_user_` token by id. Scoped to the authenticated user: a token id that isn't yours returns 404 (no-leak). Idempotent — revoking an already-revoked token also returns 404 (it is no longer a live token of yours to revoke). On success the revoked token's metadata is returned with `revoked_at` set.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.user_token_out import UserTokenOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.TokensApi(api_client)
    token_id = 'token_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Revoke one of your user-identity tokens
        api_response = api_instance.revoke_token_v0_tokens_token_id_revoke_post(token_id, authorization=authorization)
        print("The response of TokensApi->revoke_token_v0_tokens_token_id_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->revoke_token_v0_tokens_token_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**UserTokenOut**](UserTokenOut.md)

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

