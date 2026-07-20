# AgentAuthApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extensionExchangeV0AuthExtensionExchangePost**](AgentAuthApi.md#extensionexchangev0authextensionexchangepost) | **POST** /v0/auth/extension/exchange | Redeem an extension OAuth ticket for a JWT pair |
| [**initiateClaimAgentIdentityClaimPost**](AgentAuthApi.md#initiateclaimagentidentityclaimpost) | **POST** /agent/identity/claim | Initiate the human-claim ceremony for an agent identity |
| [**jwksWellKnownJwksJsonGet**](AgentAuthApi.md#jwkswellknownjwksjsonget) | **GET** /.well-known/jwks.json | JSON Web Key Set — public keys for verifying AgentDrive JWTs |
| [**oauth2TokenOauth2TokenPost**](AgentAuthApi.md#oauth2tokenoauth2tokenpost) | **POST** /oauth2/token | Exchange a credential for an access_token |
| [**oauthAuthorizationServerWellKnownOauthAuthorizationServerGet**](AgentAuthApi.md#oauthauthorizationserverwellknownoauthauthorizationserverget) | **GET** /.well-known/oauth-authorization-server | Authorization-server metadata (RFC 8414 + auth.md agent_auth block) |
| [**oauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet**](AgentAuthApi.md#oauthprotectedresourcemcpwellknownoauthprotectedresourcemcpget) | **GET** /.well-known/oauth-protected-resource/mcp | Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1) |
| [**oauthProtectedResourceWellKnownOauthProtectedResourceGet**](AgentAuthApi.md#oauthprotectedresourcewellknownoauthprotectedresourceget) | **GET** /.well-known/oauth-protected-resource | Protected-resource metadata (auth.md / RFC 9728-like discovery) |
| [**registerAgentIdentityAgentIdentityPost**](AgentAuthApi.md#registeragentidentityagentidentitypost) | **POST** /agent/identity | Register an agent identity (anonymous or ID-JAG) |



## extensionExchangeV0AuthExtensionExchangePost

> ExtensionExchangeResponse extensionExchangeV0AuthExtensionExchangePost(extensionExchangeRequest)

Redeem an extension OAuth ticket for a JWT pair

Single-use opaque ticket → JWT pair. Called once by an extension\&#39;s auth-complete.html after the OAuth handoff lands. Returns a 15-minute &#x60;access_token&#x60; (scope&#x3D;extension) and a 90-day &#x60;identity_assertion&#x60; the extension stores and refreshes via POST /oauth2/token.

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ExtensionExchangeV0AuthExtensionExchangePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  const body = {
    // ExtensionExchangeRequest
    extensionExchangeRequest: ...,
  } satisfies ExtensionExchangeV0AuthExtensionExchangePostRequest;

  try {
    const data = await api.extensionExchangeV0AuthExtensionExchangePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **extensionExchangeRequest** | [ExtensionExchangeRequest](ExtensionExchangeRequest.md) |  | |

### Return type

[**ExtensionExchangeResponse**](ExtensionExchangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## initiateClaimAgentIdentityClaimPost

> ClaimInitResponse initiateClaimAgentIdentityClaimPost(claimInitRequest)

Initiate the human-claim ceremony for an agent identity

Returns a &#x60;user_code&#x60; and &#x60;verification_uri&#x60; (RFC 8628 device-code idiom). The agent surfaces these to the human, who visits the URI, signs in, and approves the claim. The agent then polls POST /oauth2/token (grant_type&#x3D;claim) with the same &#x60;claim_token&#x60; to learn when the claim completes.

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { InitiateClaimAgentIdentityClaimPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  const body = {
    // ClaimInitRequest
    claimInitRequest: ...,
  } satisfies InitiateClaimAgentIdentityClaimPostRequest;

  try {
    const data = await api.initiateClaimAgentIdentityClaimPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **claimInitRequest** | [ClaimInitRequest](ClaimInitRequest.md) |  | |

### Return type

[**ClaimInitResponse**](ClaimInitResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## jwksWellKnownJwksJsonGet

> { [key: string]: any | null; } jwksWellKnownJwksJsonGet()

JSON Web Key Set — public keys for verifying AgentDrive JWTs

Public half of the RSA signing key for identity_assertion + access_token JWTs issued by AgentDrive. RFC 7517 shape. Cache-friendly; key rotation publishes both kids during the overlap window.

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { JwksWellKnownJwksJsonGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  try {
    const data = await api.jwksWellKnownJwksJsonGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**{ [key: string]: any | null; }**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## oauth2TokenOauth2TokenPost

> TokenResponse oauth2TokenOauth2TokenPost(grantType, assertion, claimToken)

Exchange a credential for an access_token

Two grant types:  **&#x60;urn:ietf:params:oauth:grant-type:jwt-bearer&#x60;** (RFC 7523) — body &#x60;assertion&#x3D;&lt;identity_assertion JWT&gt;&#x60;. Returns a fresh 15-minute access_token with the same scope as the assertion.  **&#x60;claim&#x60;** (custom) — body &#x60;claim_token&#x3D;&lt;from POST /agent/identity&gt;&#x60;. Polling endpoint for the claim ceremony. Returns one of: &#x60;authorization_pending&#x60; (400), &#x60;expired_token&#x60; (400), &#x60;access_denied&#x60; (400), or access_token + new identity_assertion + scope&#x3D;full (200).

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { Oauth2TokenOauth2TokenPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  const body = {
    // string
    grantType: grantType_example,
    // string (optional)
    assertion: assertion_example,
    // string (optional)
    claimToken: claimToken_example,
  } satisfies Oauth2TokenOauth2TokenPostRequest;

  try {
    const data = await api.oauth2TokenOauth2TokenPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **grantType** | `string` |  | [Defaults to `undefined`] |
| **assertion** | `string` |  | [Optional] [Defaults to `undefined`] |
| **claimToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## oauthAuthorizationServerWellKnownOauthAuthorizationServerGet

> { [key: string]: any | null; } oauthAuthorizationServerWellKnownOauthAuthorizationServerGet()

Authorization-server metadata (RFC 8414 + auth.md agent_auth block)

Discovery document for the auth.md protocol. Carries the standard RFC 8414 fields plus an &#x60;agent_auth&#x60; block per the auth.md spec — the latter is what an agent runtime keys off to find the identity + claim endpoints.

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { OauthAuthorizationServerWellKnownOauthAuthorizationServerGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  try {
    const data = await api.oauthAuthorizationServerWellKnownOauthAuthorizationServerGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**{ [key: string]: any | null; }**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## oauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet

> { [key: string]: any | null; } oauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet()

Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1)

Path-inserted variant of the protected-resource document. MCP clients derive this URL from the resource URL &#x60;{origin}/mcp&#x60; (RFC 9728 §3.1: insert the well-known segment between host and path) after reading the WWW-Authenticate challenge on a 401 — it is the first hop of the client-side OAuth flow.

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  try {
    const data = await api.oauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**{ [key: string]: any | null; }**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## oauthProtectedResourceWellKnownOauthProtectedResourceGet

> { [key: string]: any | null; } oauthProtectedResourceWellKnownOauthProtectedResourceGet()

Protected-resource metadata (auth.md / RFC 9728-like discovery)

Names this server as a protected resource and points clients at the authorization server they should obtain tokens from. In this design the resource server and authorization server are the same host.

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { OauthProtectedResourceWellKnownOauthProtectedResourceGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  try {
    const data = await api.oauthProtectedResourceWellKnownOauthProtectedResourceGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**{ [key: string]: any | null; }**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## registerAgentIdentityAgentIdentityPost

> AnonymousIdentityResponse registerAgentIdentityAgentIdentityPost(requestBody)

Register an agent identity (anonymous or ID-JAG)

Two registration modes:  **&#x60;type&#x3D;anonymous&#x60;** — Provisions a brand-new agent identity bound to a fresh shadow-org drive. No human involved; returned &#x60;identity_assertion&#x60; carries &#x60;scope&#x3D;pre_claim&#x60;. A human completes the claim ceremony later via /claim.  **&#x60;type&#x3D;identity_assertion&#x60;** — Agent provider (e.g. WorkOS) has already minted an ID-JAG asserting a user identity binding. We verify it against the provider\&#39;s JWKS and provision a **claimed** identity immediately: scope&#x3D;full, drive bound to the user, no claim ceremony needed.

### Example

```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RegisterAgentIdentityAgentIdentityPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  const body = {
    // { [key: string]: any | null; }
    requestBody: Object,
  } satisfies RegisterAgentIdentityAgentIdentityPostRequest;

  try {
    const data = await api.registerAgentIdentityAgentIdentityPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **requestBody** | `{ [key: string]: any | null; }` |  | |

### Return type

[**AnonymousIdentityResponse**](AnonymousIdentityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

