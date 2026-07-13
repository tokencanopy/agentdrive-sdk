# \MembersAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**InviteMemberV0MembersInvitePost**](MembersAPI.md#InviteMemberV0MembersInvitePost) | **Post** /v0/members/invite | Invite a person to your workspace by email
[**ListInvitationsV0InvitationsGet**](MembersAPI.md#ListInvitationsV0InvitationsGet) | **Get** /v0/invitations | List pending invitations
[**ListMembersV0MembersGet**](MembersAPI.md#ListMembersV0MembersGet) | **Get** /v0/members | List the members of your active workspace
[**RemoveMemberV0MembersTargetUserIdDelete**](MembersAPI.md#RemoveMemberV0MembersTargetUserIdDelete) | **Delete** /v0/members/{target_user_id} | Remove a member (or leave)
[**RevokeInvitationV0InvitationsInvitationIdDelete**](MembersAPI.md#RevokeInvitationV0InvitationsInvitationIdDelete) | **Delete** /v0/invitations/{invitation_id} | Revoke a pending invitation
[**SetMemberRoleV0MembersTargetUserIdPatch**](MembersAPI.md#SetMemberRoleV0MembersTargetUserIdPatch) | **Patch** /v0/members/{target_user_id} | Change a member&#39;s role



## InviteMemberV0MembersInvitePost

> InviteCreateOut InviteMemberV0MembersInvitePost(ctx).MemberInviteIn(memberInviteIn).Authorization(authorization).Execute()

Invite a person to your workspace by email



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {
	memberInviteIn := *openapiclient.NewMemberInviteIn("Email_example") // MemberInviteIn | 
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.InviteMemberV0MembersInvitePost(context.Background()).MemberInviteIn(memberInviteIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.InviteMemberV0MembersInvitePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `InviteMemberV0MembersInvitePost`: InviteCreateOut
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.InviteMemberV0MembersInvitePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiInviteMemberV0MembersInvitePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memberInviteIn** | [**MemberInviteIn**](MemberInviteIn.md) |  | 
 **authorization** | **string** |  | 

### Return type

[**InviteCreateOut**](InviteCreateOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListInvitationsV0InvitationsGet

> InvitationList ListInvitationsV0InvitationsGet(ctx).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

List pending invitations



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.ListInvitationsV0InvitationsGet(context.Background()).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.ListInvitationsV0InvitationsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListInvitationsV0InvitationsGet`: InvitationList
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.ListInvitationsV0InvitationsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListInvitationsV0InvitationsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **string** |  | 
 **limit** | **int32** |  | 
 **authorization** | **string** |  | 

### Return type

[**InvitationList**](InvitationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListMembersV0MembersGet

> MemberList ListMembersV0MembersGet(ctx).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

List the members of your active workspace



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.ListMembersV0MembersGet(context.Background()).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.ListMembersV0MembersGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMembersV0MembersGet`: MemberList
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.ListMembersV0MembersGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListMembersV0MembersGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **string** |  | 
 **limit** | **int32** |  | 
 **authorization** | **string** |  | 

### Return type

[**MemberList**](MemberList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RemoveMemberV0MembersTargetUserIdDelete

> MemberRemoveOut RemoveMemberV0MembersTargetUserIdDelete(ctx, targetUserId).Confirm(confirm).Authorization(authorization).Execute()

Remove a member (or leave)



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {
	targetUserId := "targetUserId_example" // string | 
	confirm := "confirm_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.RemoveMemberV0MembersTargetUserIdDelete(context.Background(), targetUserId).Confirm(confirm).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.RemoveMemberV0MembersTargetUserIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RemoveMemberV0MembersTargetUserIdDelete`: MemberRemoveOut
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.RemoveMemberV0MembersTargetUserIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**targetUserId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRemoveMemberV0MembersTargetUserIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **confirm** | **string** |  | 
 **authorization** | **string** |  | 

### Return type

[**MemberRemoveOut**](MemberRemoveOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeInvitationV0InvitationsInvitationIdDelete

> RevokeOut RevokeInvitationV0InvitationsInvitationIdDelete(ctx, invitationId).Authorization(authorization).Execute()

Revoke a pending invitation



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {
	invitationId := "invitationId_example" // string | 
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.RevokeInvitationV0InvitationsInvitationIdDelete(context.Background(), invitationId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.RevokeInvitationV0InvitationsInvitationIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeInvitationV0InvitationsInvitationIdDelete`: RevokeOut
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.RevokeInvitationV0InvitationsInvitationIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**invitationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRevokeInvitationV0InvitationsInvitationIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **authorization** | **string** |  | 

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SetMemberRoleV0MembersTargetUserIdPatch

> MemberOut SetMemberRoleV0MembersTargetUserIdPatch(ctx, targetUserId).MemberRoleIn(memberRoleIn).Authorization(authorization).Execute()

Change a member's role



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {
	targetUserId := "targetUserId_example" // string | 
	memberRoleIn := *openapiclient.NewMemberRoleIn("Role_example") // MemberRoleIn | 
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.SetMemberRoleV0MembersTargetUserIdPatch(context.Background(), targetUserId).MemberRoleIn(memberRoleIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.SetMemberRoleV0MembersTargetUserIdPatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SetMemberRoleV0MembersTargetUserIdPatch`: MemberOut
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.SetMemberRoleV0MembersTargetUserIdPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**targetUserId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSetMemberRoleV0MembersTargetUserIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **memberRoleIn** | [**MemberRoleIn**](MemberRoleIn.md) |  | 
 **authorization** | **string** |  | 

### Return type

[**MemberOut**](MemberOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

