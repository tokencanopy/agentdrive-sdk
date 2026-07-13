# agentdrive_sdk.MembersApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invite_member_v0_members_invite_post**](MembersApi.md#invite_member_v0_members_invite_post) | **POST** /v0/members/invite | Invite a person to your workspace by email
[**list_invitations_v0_invitations_get**](MembersApi.md#list_invitations_v0_invitations_get) | **GET** /v0/invitations | List pending invitations
[**list_members_v0_members_get**](MembersApi.md#list_members_v0_members_get) | **GET** /v0/members | List the members of your active workspace
[**remove_member_v0_members_target_user_id_delete**](MembersApi.md#remove_member_v0_members_target_user_id_delete) | **DELETE** /v0/members/{target_user_id} | Remove a member (or leave)
[**revoke_invitation_v0_invitations_invitation_id_delete**](MembersApi.md#revoke_invitation_v0_invitations_invitation_id_delete) | **DELETE** /v0/invitations/{invitation_id} | Revoke a pending invitation
[**set_member_role_v0_members_target_user_id_patch**](MembersApi.md#set_member_role_v0_members_target_user_id_patch) | **PATCH** /v0/members/{target_user_id} | Change a member&#39;s role


# **invite_member_v0_members_invite_post**
> InviteCreateOut invite_member_v0_members_invite_post(member_invite_in, authorization=authorization)

Invite a person to your workspace by email

Create a pending invitation in the caller's active workspace and enqueue the invite email. **Admin only**, `full` scope. Inviting an existing member is a no-op success (`already_member: true`). A duplicate pending invite for the same email returns 409 `INVITE_PENDING` (resend it from the members page). The raw invite token is delivered only by email — never in this response.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.invite_create_out import InviteCreateOut
from agentdrive_sdk.models.member_invite_in import MemberInviteIn
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
    api_instance = agentdrive_sdk.MembersApi(api_client)
    member_invite_in = agentdrive_sdk.MemberInviteIn() # MemberInviteIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Invite a person to your workspace by email
        api_response = api_instance.invite_member_v0_members_invite_post(member_invite_in, authorization=authorization)
        print("The response of MembersApi->invite_member_v0_members_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->invite_member_v0_members_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_invite_in** | [**MemberInviteIn**](MemberInviteIn.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**InviteCreateOut**](InviteCreateOut.md)

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

# **list_invitations_v0_invitations_get**
> InvitationList list_invitations_v0_invitations_get(cursor=cursor, limit=limit, authorization=authorization)

List pending invitations

List the pending invitations for the caller's active workspace. **Admin only.** Metadata only — the raw invite token is never surfaced.

Newest first (`created_at` descending, tie-broken by `id`). Paginated: `limit` is clamped to [1, 100] (default 50, never a 422); pass the response's `next_cursor` back as `cursor` for the next page (`null` when the listing is complete).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.invitation_list import InvitationList
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
    api_instance = agentdrive_sdk.MembersApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List pending invitations
        api_response = api_instance.list_invitations_v0_invitations_get(cursor=cursor, limit=limit, authorization=authorization)
        print("The response of MembersApi->list_invitations_v0_invitations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->list_invitations_v0_invitations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**InvitationList**](InvitationList.md)

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

# **list_members_v0_members_get**
> MemberList list_members_v0_members_get(cursor=cursor, limit=limit, authorization=authorization)

List the members of your active workspace

List live members (email, role, joined-at) of the caller's active workspace. Any **member** may list; a `read`-scope token is sufficient.

Ordered by join time (`created_at`, tie-broken by `user_id`) — **no role grouping is promised**; a dashboard that wants admins-first sorts client-side. Paginated: `limit` is clamped to [1, 100] (default 50, never a 422); pass the response's `next_cursor` back as `cursor` for the next page (`null` when the listing is complete).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.member_list import MemberList
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
    api_instance = agentdrive_sdk.MembersApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List the members of your active workspace
        api_response = api_instance.list_members_v0_members_get(cursor=cursor, limit=limit, authorization=authorization)
        print("The response of MembersApi->list_members_v0_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->list_members_v0_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**MemberList**](MemberList.md)

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

# **remove_member_v0_members_target_user_id_delete**
> MemberRemoveOut remove_member_v0_members_target_user_id_delete(target_user_id, confirm=confirm, authorization=authorization)

Remove a member (or leave)

Remove a member from the caller's active workspace, soft-deleting every drive that member owns there (workspaces-design §4.4 — no ownership transfer in v0; their `ad_live_` keys then stop working). **Admin** may remove anyone; **any member** may remove themselves (self-leave). `full` scope. Removing the **last/sole admin** is rejected with 409 `LAST_ADMIN` (promote someone first, or delete the workspace).

**Explicit confirmation required:** pass `?confirm=DELETE` or the request is rejected with 400 `CONFIRM_REQUIRED` — removal cascades a soft-delete of every drive the member owns, so it carries tenant-level blast radius (uniform with `DELETE /v0/drives/{id}`).

Deliberately takes NO `If-Match`: membership rows carry no generation/metageneration axis to pin (there is no ETag to echo), so `?confirm=DELETE` is the sole mutation guard here.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.member_remove_out import MemberRemoveOut
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
    api_instance = agentdrive_sdk.MembersApi(api_client)
    target_user_id = 'target_user_id_example' # str | 
    confirm = 'confirm_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Remove a member (or leave)
        api_response = api_instance.remove_member_v0_members_target_user_id_delete(target_user_id, confirm=confirm, authorization=authorization)
        print("The response of MembersApi->remove_member_v0_members_target_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->remove_member_v0_members_target_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_user_id** | **str**|  | 
 **confirm** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**MemberRemoveOut**](MemberRemoveOut.md)

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

# **revoke_invitation_v0_invitations_invitation_id_delete**
> RevokeOut revoke_invitation_v0_invitations_invitation_id_delete(invitation_id, authorization=authorization)

Revoke a pending invitation

Revoke a pending invitation in the caller's active workspace. **Admin only**, `full` scope. Org-scoped + idempotent: `revoked` is a COUNT — 1 when a live invite was revoked, 0 when it was already gone (a forged id, an invite from another workspace, or an already-consumed invite all return `revoked: 0`, no-leak).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.revoke_out import RevokeOut
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
    api_instance = agentdrive_sdk.MembersApi(api_client)
    invitation_id = 'invitation_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Revoke a pending invitation
        api_response = api_instance.revoke_invitation_v0_invitations_invitation_id_delete(invitation_id, authorization=authorization)
        print("The response of MembersApi->revoke_invitation_v0_invitations_invitation_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->revoke_invitation_v0_invitations_invitation_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**RevokeOut**](RevokeOut.md)

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

# **set_member_role_v0_members_target_user_id_patch**
> MemberOut set_member_role_v0_members_target_user_id_patch(target_user_id, member_role_in, authorization=authorization)

Change a member's role

Promote/demote a member in the caller's active workspace. **Admin only**, `full` scope. Demoting the workspace's **last admin** is rejected with 409 `LAST_ADMIN` (promote someone first).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.member_out import MemberOut
from agentdrive_sdk.models.member_role_in import MemberRoleIn
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
    api_instance = agentdrive_sdk.MembersApi(api_client)
    target_user_id = 'target_user_id_example' # str | 
    member_role_in = agentdrive_sdk.MemberRoleIn() # MemberRoleIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Change a member's role
        api_response = api_instance.set_member_role_v0_members_target_user_id_patch(target_user_id, member_role_in, authorization=authorization)
        print("The response of MembersApi->set_member_role_v0_members_target_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->set_member_role_v0_members_target_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_user_id** | **str**|  | 
 **member_role_in** | [**MemberRoleIn**](MemberRoleIn.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**MemberOut**](MemberOut.md)

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

