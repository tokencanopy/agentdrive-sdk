# agentdrive_sdk.TokensApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tokens_v0_tokens_get**](TokensApi.md#list_tokens_v0_tokens_get) | **GET** /v0/tokens | List your user-identity tokens
[**revoke_token_v0_tokens_token_id_revoke_post**](TokensApi.md#revoke_token_v0_tokens_token_id_revoke_post) | **POST** /v0/tokens/{token_id}/revoke | Revoke one of your user-identity tokens


# **list_tokens_v0_tokens_get**
> UserTokenList list_tokens_v0_tokens_get(cursor=cursor, limit=limit)

List your user-identity tokens

List the `ad_user_` tokens belonging to the authenticated user. Metadata only — the raw token is shown once at mint (web only) and is never returned here. Includes recently-revoked tokens (with `revoked_at` set) so the caller can audit them; newest first.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.TokensApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List your user-identity tokens
        api_response = api_instance.list_tokens_v0_tokens_get(cursor=cursor, limit=limit)
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

### Return type

[**UserTokenList**](UserTokenList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token_v0_tokens_token_id_revoke_post**
> UserTokenOut revoke_token_v0_tokens_token_id_revoke_post(token_id)

Revoke one of your user-identity tokens

Revoke a single `ad_user_` token by id. Scoped to the authenticated user: a token id that isn't yours returns 404 (no-leak). Idempotent — revoking an already-revoked token also returns 404 (it is no longer a live token of yours to revoke). On success the revoked token's metadata is returned with `revoked_at` set.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.TokensApi(api_client)
    token_id = 'token_id_example' # str |

    try:
        # Revoke one of your user-identity tokens
        api_response = api_instance.revoke_token_v0_tokens_token_id_revoke_post(token_id)
        print("The response of TokensApi->revoke_token_v0_tokens_token_id_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->revoke_token_v0_tokens_token_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  |

### Return type

[**UserTokenOut**](UserTokenOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The token does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
