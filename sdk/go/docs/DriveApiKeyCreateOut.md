# DriveApiKeyCreateOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**ApiKey** | **string** |  | 
**Prefix** | **string** |  | 
**Label** | **NullableString** |  | 
**CreatedAt** | **time.Time** |  | 

## Methods

### NewDriveApiKeyCreateOut

`func NewDriveApiKeyCreateOut(id string, apiKey string, prefix string, label NullableString, createdAt time.Time, ) *DriveApiKeyCreateOut`

NewDriveApiKeyCreateOut instantiates a new DriveApiKeyCreateOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveApiKeyCreateOutWithDefaults

`func NewDriveApiKeyCreateOutWithDefaults() *DriveApiKeyCreateOut`

NewDriveApiKeyCreateOutWithDefaults instantiates a new DriveApiKeyCreateOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DriveApiKeyCreateOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DriveApiKeyCreateOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DriveApiKeyCreateOut) SetId(v string)`

SetId sets Id field to given value.


### GetApiKey

`func (o *DriveApiKeyCreateOut) GetApiKey() string`

GetApiKey returns the ApiKey field if non-nil, zero value otherwise.

### GetApiKeyOk

`func (o *DriveApiKeyCreateOut) GetApiKeyOk() (*string, bool)`

GetApiKeyOk returns a tuple with the ApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKey

`func (o *DriveApiKeyCreateOut) SetApiKey(v string)`

SetApiKey sets ApiKey field to given value.


### GetPrefix

`func (o *DriveApiKeyCreateOut) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *DriveApiKeyCreateOut) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *DriveApiKeyCreateOut) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *DriveApiKeyCreateOut) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *DriveApiKeyCreateOut) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *DriveApiKeyCreateOut) SetLabel(v string)`

SetLabel sets Label field to given value.


### SetLabelNil

`func (o *DriveApiKeyCreateOut) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *DriveApiKeyCreateOut) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetCreatedAt

`func (o *DriveApiKeyCreateOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DriveApiKeyCreateOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DriveApiKeyCreateOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


