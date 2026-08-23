# \SharesRedemptionAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SharesRedeem**](SharesRedemptionAPI.md#SharesRedeem) | **Get** /s/{share_key} | Redeem Share



## SharesRedeem

> interface{} SharesRedeem(ctx, shareKey).Execute()

Redeem Share



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
	shareKey := "shareKey_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SharesRedemptionAPI.SharesRedeem(context.Background(), shareKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SharesRedemptionAPI.SharesRedeem``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SharesRedeem`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SharesRedemptionAPI.SharesRedeem`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**shareKey** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSharesRedeemRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
