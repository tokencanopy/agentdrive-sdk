# MembersApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**inviteMemberV0MembersInvitePost**](MembersApi.md#invitememberv0membersinvitepost) | **POST** /v0/members/invite | Invite a person to your workspace by email |
| [**listInvitationsV0InvitationsGet**](MembersApi.md#listinvitationsv0invitationsget) | **GET** /v0/invitations | List pending invitations |
| [**listMembersV0MembersGet**](MembersApi.md#listmembersv0membersget) | **GET** /v0/members | List the members of your active workspace |
| [**removeMemberV0MembersTargetUserIdDelete**](MembersApi.md#removememberv0memberstargetuseriddelete) | **DELETE** /v0/members/{target_user_id} | Remove a member (or leave) |
| [**revokeInvitationV0InvitationsInvitationIdDelete**](MembersApi.md#revokeinvitationv0invitationsinvitationiddelete) | **DELETE** /v0/invitations/{invitation_id} | Revoke a pending invitation |
| [**setMemberRoleV0MembersTargetUserIdPatch**](MembersApi.md#setmemberrolev0memberstargetuseridpatch) | **PATCH** /v0/members/{target_user_id} | Change a member\&#39;s role |



## inviteMemberV0MembersInvitePost

> InviteCreateOut inviteMemberV0MembersInvitePost(memberInviteIn)

Invite a person to your workspace by email

Create a pending invitation in the caller\&#39;s active workspace and enqueue the invite email. **Admin only**, &#x60;full&#x60; scope. Inviting an existing member is a no-op success (&#x60;already_member: true&#x60;). A duplicate pending invite for the same email returns 409 &#x60;INVITE_PENDING&#x60; (resend it from the members page). The raw invite token is delivered only by email — never in this response.

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { InviteMemberV0MembersInvitePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // MemberInviteIn
    memberInviteIn: ...,
  } satisfies InviteMemberV0MembersInvitePostRequest;

  try {
    const data = await api.inviteMemberV0MembersInvitePost(body);
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
| **memberInviteIn** | [MemberInviteIn](MemberInviteIn.md) |  | |

### Return type

[**InviteCreateOut**](InviteCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The email or role is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The user is already a member or has a pending invitation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listInvitationsV0InvitationsGet

> InvitationList listInvitationsV0InvitationsGet(cursor, limit)

List pending invitations

List the pending invitations for the caller\&#39;s active workspace. **Admin only.** Metadata only — the raw invite token is never surfaced.  Newest first (&#x60;created_at&#x60; descending, tie-broken by &#x60;id&#x60;). Paginated: &#x60;limit&#x60; is clamped to [1, 100] (default 50, never a 422); pass the response\&#39;s &#x60;next_cursor&#x60; back as &#x60;cursor&#x60; for the next page (&#x60;null&#x60; when the listing is complete).

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListInvitationsV0InvitationsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListInvitationsV0InvitationsGetRequest;

  try {
    const data = await api.listInvitationsV0InvitationsGet(body);
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
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**InvitationList**](InvitationList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listMembersV0MembersGet

> MemberList listMembersV0MembersGet(cursor, limit)

List the members of your active workspace

List live members (email, role, joined-at) of the caller\&#39;s active workspace. Any **member** may list; a &#x60;read&#x60;-scope token is sufficient.  Ordered by join time (&#x60;created_at&#x60;, tie-broken by &#x60;user_id&#x60;) — **no role grouping is promised**; a dashboard that wants admins-first sorts client-side. Paginated: &#x60;limit&#x60; is clamped to [1, 100] (default 50, never a 422); pass the response\&#39;s &#x60;next_cursor&#x60; back as &#x60;cursor&#x60; for the next page (&#x60;null&#x60; when the listing is complete).

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListMembersV0MembersGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListMembersV0MembersGetRequest;

  try {
    const data = await api.listMembersV0MembersGet(body);
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
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**MemberList**](MemberList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## removeMemberV0MembersTargetUserIdDelete

> MemberRemoveOut removeMemberV0MembersTargetUserIdDelete(targetUserId, confirm)

Remove a member (or leave)

Remove a member from the caller\&#39;s active workspace, soft-deleting every drive that member owns there (workspaces-design §4.4 — no ownership transfer in v0; their &#x60;ad_live_&#x60; keys then stop working). **Admin** may remove anyone; **any member** may remove themselves (self-leave). &#x60;full&#x60; scope. Removing the **last/sole admin** is rejected with 409 &#x60;LAST_ADMIN&#x60; (promote someone first, or delete the workspace).  **Explicit confirmation required:** pass &#x60;?confirm&#x3D;DELETE&#x60; or the request is rejected with 400 &#x60;CONFIRM_REQUIRED&#x60; — removal cascades a soft-delete of every drive the member owns, so it carries tenant-level blast radius (uniform with &#x60;DELETE /v0/drives/{id}&#x60;).  Deliberately takes NO &#x60;If-Match&#x60;: membership rows carry no generation/metageneration axis to pin (there is no ETag to echo), so &#x60;?confirm&#x3D;DELETE&#x60; is the sole mutation guard here.

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RemoveMemberV0MembersTargetUserIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    targetUserId: targetUserId_example,
    // string (optional)
    confirm: confirm_example,
  } satisfies RemoveMemberV0MembersTargetUserIdDeleteRequest;

  try {
    const data = await api.removeMemberV0MembersTargetUserIdDelete(body);
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
| **targetUserId** | `string` |  | [Defaults to `undefined`] |
| **confirm** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**MemberRemoveOut**](MemberRemoveOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The member does not exist in this workspace. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The removal would violate workspace ownership requirements. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## revokeInvitationV0InvitationsInvitationIdDelete

> RevokeOut revokeInvitationV0InvitationsInvitationIdDelete(invitationId)

Revoke a pending invitation

Revoke a pending invitation in the caller\&#39;s active workspace. **Admin only**, &#x60;full&#x60; scope. Org-scoped + idempotent: &#x60;revoked&#x60; is a COUNT — 1 when a live invite was revoked, 0 when it was already gone (a forged id, an invite from another workspace, or an already-consumed invite all return &#x60;revoked: 0&#x60;, no-leak).

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeInvitationV0InvitationsInvitationIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    invitationId: invitationId_example,
  } satisfies RevokeInvitationV0InvitationsInvitationIdDeleteRequest;

  try {
    const data = await api.revokeInvitationV0InvitationsInvitationIdDelete(body);
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
| **invitationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The invitation does not exist in this workspace. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## setMemberRoleV0MembersTargetUserIdPatch

> MemberOut setMemberRoleV0MembersTargetUserIdPatch(targetUserId, memberRoleIn)

Change a member\&#39;s role

Promote/demote a member in the caller\&#39;s active workspace. **Admin only**, &#x60;full&#x60; scope. Demoting the workspace\&#39;s **last admin** is rejected with 409 &#x60;LAST_ADMIN&#x60; (promote someone first).

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SetMemberRoleV0MembersTargetUserIdPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    targetUserId: targetUserId_example,
    // MemberRoleIn
    memberRoleIn: ...,
  } satisfies SetMemberRoleV0MembersTargetUserIdPatchRequest;

  try {
    const data = await api.setMemberRoleV0MembersTargetUserIdPatch(body);
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
| **targetUserId** | `string` |  | [Defaults to `undefined`] |
| **memberRoleIn** | [MemberRoleIn](MemberRoleIn.md) |  | |

### Return type

[**MemberOut**](MemberOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The membership update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The member does not exist in this workspace. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The update would violate workspace ownership requirements. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
