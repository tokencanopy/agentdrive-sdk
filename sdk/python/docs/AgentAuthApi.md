# agentdrive_sdk.AgentAuthApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extension_exchange_v0_auth_extension_exchange_post**](AgentAuthApi.md#extension_exchange_v0_auth_extension_exchange_post) | **POST** /v0/auth/extension/exchange | Redeem an extension OAuth ticket for a JWT pair
[**initiate_claim_agent_identity_claim_post**](AgentAuthApi.md#initiate_claim_agent_identity_claim_post) | **POST** /agent/identity/claim | Initiate the human-claim ceremony for an agent identity
[**jwks_well_known_jwks_json_get**](AgentAuthApi.md#jwks_well_known_jwks_json_get) | **GET** /.well-known/jwks.json | JSON Web Key Set — public keys for verifying AgentDrive JWTs
[**oauth2_token_oauth2_token_post**](AgentAuthApi.md#oauth2_token_oauth2_token_post) | **POST** /oauth2/token | Exchange a credential for an access_token
[**oauth_authorization_server_well_known_oauth_authorization_server_get**](AgentAuthApi.md#oauth_authorization_server_well_known_oauth_authorization_server_get) | **GET** /.well-known/oauth-authorization-server | Authorization-server metadata (RFC 8414 + auth.md agent_auth block)
[**oauth_protected_resource_mcp_well_known_oauth_protected_resource_mcp_get**](AgentAuthApi.md#oauth_protected_resource_mcp_well_known_oauth_protected_resource_mcp_get) | **GET** /.well-known/oauth-protected-resource/mcp | Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1)
[**oauth_protected_resource_well_known_oauth_protected_resource_get**](AgentAuthApi.md#oauth_protected_resource_well_known_oauth_protected_resource_get) | **GET** /.well-known/oauth-protected-resource | Protected-resource metadata (auth.md / RFC 9728-like discovery)
[**register_agent_identity_agent_identity_post**](AgentAuthApi.md#register_agent_identity_agent_identity_post) | **POST** /agent/identity | Register an agent identity (anonymous or ID-JAG)


# **extension_exchange_v0_auth_extension_exchange_post**
> ExtensionExchangeResponse extension_exchange_v0_auth_extension_exchange_post(extension_exchange_request)

Redeem an extension OAuth ticket for a JWT pair

Single-use opaque ticket → JWT pair. Called once by an extension's auth-complete.html after the OAuth handoff lands. Returns a 15-minute `access_token` (scope=extension) and a 90-day `identity_assertion` the extension stores and refreshes via POST /oauth2/token.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.extension_exchange_request import ExtensionExchangeRequest
from agentdrive_sdk.models.extension_exchange_response import ExtensionExchangeResponse
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)
    extension_exchange_request = agentdrive_sdk.ExtensionExchangeRequest() # ExtensionExchangeRequest |

    try:
        # Redeem an extension OAuth ticket for a JWT pair
        api_response = api_instance.extension_exchange_v0_auth_extension_exchange_post(extension_exchange_request)
        print("The response of AgentAuthApi->extension_exchange_v0_auth_extension_exchange_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->extension_exchange_v0_auth_extension_exchange_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_exchange_request** | [**ExtensionExchangeRequest**](ExtensionExchangeRequest.md)|  |

### Return type

[**ExtensionExchangeResponse**](ExtensionExchangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The extension ID or ticket is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Too many extension sign-in attempts. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Extension authentication or token signing is unavailable. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_claim_agent_identity_claim_post**
> ClaimInitResponse initiate_claim_agent_identity_claim_post(claim_init_request)

Initiate the human-claim ceremony for an agent identity

Returns a `user_code` and `verification_uri` (RFC 8628 device-code idiom). The agent surfaces these to the human, who visits the URI, signs in, and approves the claim. The agent then polls POST /oauth2/token (grant_type=claim) with the same `claim_token` to learn when the claim completes.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.claim_init_request import ClaimInitRequest
from agentdrive_sdk.models.claim_init_response import ClaimInitResponse
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)
    claim_init_request = agentdrive_sdk.ClaimInitRequest() # ClaimInitRequest |

    try:
        # Initiate the human-claim ceremony for an agent identity
        api_response = api_instance.initiate_claim_agent_identity_claim_post(claim_init_request)
        print("The response of AgentAuthApi->initiate_claim_agent_identity_claim_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->initiate_claim_agent_identity_claim_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **claim_init_request** | [**ClaimInitRequest**](ClaimInitRequest.md)|  |

### Return type

[**ClaimInitResponse**](ClaimInitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jwks_well_known_jwks_json_get**
> JwksOut jwks_well_known_jwks_json_get()

JSON Web Key Set — public keys for verifying AgentDrive JWTs

Public half of the RSA signing key for identity_assertion + access_token JWTs issued by AgentDrive. RFC 7517 shape. Cache-friendly; key rotation publishes both kids during the overlap window.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.jwks_out import JwksOut
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)

    try:
        # JSON Web Key Set — public keys for verifying AgentDrive JWTs
        api_response = api_instance.jwks_well_known_jwks_json_get()
        print("The response of AgentAuthApi->jwks_well_known_jwks_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->jwks_well_known_jwks_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JwksOut**](JwksOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_token_oauth2_token_post**
> TokenResponse oauth2_token_oauth2_token_post(grant_type, assertion=assertion, claim_token=claim_token)

Exchange a credential for an access_token

Two grant types:

**`urn:ietf:params:oauth:grant-type:jwt-bearer`** (RFC 7523) — body `assertion=<identity_assertion JWT>`. Returns a fresh 15-minute access_token with the same scope as the assertion.

**`claim`** (custom) — body `claim_token=<from POST /agent/identity>`. Polling endpoint for the claim ceremony. Returns one of: `authorization_pending` (400), `expired_token` (400), `access_denied` (400), or access_token + new identity_assertion + scope=full (200).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.token_response import TokenResponse
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)
    grant_type = 'grant_type_example' # str |
    assertion = 'assertion_example' # str |  (optional)
    claim_token = 'claim_token_example' # str |  (optional)

    try:
        # Exchange a credential for an access_token
        api_response = api_instance.oauth2_token_oauth2_token_post(grant_type, assertion=assertion, claim_token=claim_token)
        print("The response of AgentAuthApi->oauth2_token_oauth2_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->oauth2_token_oauth2_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  |
 **assertion** | **str**|  | [optional]
 **claim_token** | **str**|  | [optional]

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_authorization_server_well_known_oauth_authorization_server_get**
> AuthorizationServerMetadataOut oauth_authorization_server_well_known_oauth_authorization_server_get()

Authorization-server metadata (RFC 8414 + auth.md agent_auth block)

Discovery document for the auth.md protocol. Carries the standard RFC 8414 fields plus an `agent_auth` block per the auth.md spec — the latter is what an agent runtime keys off to find the identity + claim endpoints.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.authorization_server_metadata_out import AuthorizationServerMetadataOut
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)

    try:
        # Authorization-server metadata (RFC 8414 + auth.md agent_auth block)
        api_response = api_instance.oauth_authorization_server_well_known_oauth_authorization_server_get()
        print("The response of AgentAuthApi->oauth_authorization_server_well_known_oauth_authorization_server_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->oauth_authorization_server_well_known_oauth_authorization_server_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthorizationServerMetadataOut**](AuthorizationServerMetadataOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_protected_resource_mcp_well_known_oauth_protected_resource_mcp_get**
> ProtectedResourceMetadataOut oauth_protected_resource_mcp_well_known_oauth_protected_resource_mcp_get()

Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1)

Path-inserted variant of the protected-resource document. MCP clients derive this URL from the resource URL `{origin}/mcp` (RFC 9728 §3.1: insert the well-known segment between host and path) after reading the WWW-Authenticate challenge on a 401 — it is the first hop of the client-side OAuth flow.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.protected_resource_metadata_out import ProtectedResourceMetadataOut
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)

    try:
        # Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1)
        api_response = api_instance.oauth_protected_resource_mcp_well_known_oauth_protected_resource_mcp_get()
        print("The response of AgentAuthApi->oauth_protected_resource_mcp_well_known_oauth_protected_resource_mcp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->oauth_protected_resource_mcp_well_known_oauth_protected_resource_mcp_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProtectedResourceMetadataOut**](ProtectedResourceMetadataOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_protected_resource_well_known_oauth_protected_resource_get**
> ProtectedResourceMetadataOut oauth_protected_resource_well_known_oauth_protected_resource_get()

Protected-resource metadata (auth.md / RFC 9728-like discovery)

Names this server as a protected resource and points clients at the authorization server they should obtain tokens from. In this design the resource server and authorization server are the same host.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.protected_resource_metadata_out import ProtectedResourceMetadataOut
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)

    try:
        # Protected-resource metadata (auth.md / RFC 9728-like discovery)
        api_response = api_instance.oauth_protected_resource_well_known_oauth_protected_resource_get()
        print("The response of AgentAuthApi->oauth_protected_resource_well_known_oauth_protected_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->oauth_protected_resource_well_known_oauth_protected_resource_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProtectedResourceMetadataOut**](ProtectedResourceMetadataOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_agent_identity_agent_identity_post**
> AnonymousIdentityResponse register_agent_identity_agent_identity_post(request_body)

Register an agent identity (anonymous or ID-JAG)

Two registration modes:

**`type=anonymous`** — Provisions a brand-new agent identity bound to a fresh shadow-org drive. No human involved; returned `identity_assertion` carries `scope=pre_claim`. A human completes the claim ceremony later via /claim.

**`type=identity_assertion`** — Agent provider (e.g. WorkOS) has already minted an ID-JAG asserting a user identity binding. We verify it against the provider's JWKS and provision a **claimed** identity immediately: scope=full, drive bound to the user, no claim ceremony needed.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.anonymous_identity_response import AnonymousIdentityResponse
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
    api_instance = agentdrive_sdk.AgentAuthApi(api_client)
    request_body = None # Dict[str, Optional[object]] |

    try:
        # Register an agent identity (anonymous or ID-JAG)
        api_response = api_instance.register_agent_identity_agent_identity_post(request_body)
        print("The response of AgentAuthApi->register_agent_identity_agent_identity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAuthApi->register_agent_identity_agent_identity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  |

### Return type

[**AnonymousIdentityResponse**](AnonymousIdentityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Agent identity signing is not configured. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
