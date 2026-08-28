# WorkbookOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtifactId** | **string** |  |
**CellCount** | **int32** |  |
**Editability** | [**EditabilityOut**](EditabilityOut.md) |  |
**Format** | **string** |  |
**Revision** | **string** |  |

## Methods

### NewWorkbookOut

`func NewWorkbookOut(artifactId string, cellCount int32, editability EditabilityOut, format string, revision string, ) *WorkbookOut`

NewWorkbookOut instantiates a new WorkbookOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWorkbookOutWithDefaults

`func NewWorkbookOutWithDefaults() *WorkbookOut`

NewWorkbookOutWithDefaults instantiates a new WorkbookOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtifactId

`func (o *WorkbookOut) GetArtifactId() string`

GetArtifactId returns the ArtifactId field if non-nil, zero value otherwise.

### GetArtifactIdOk

`func (o *WorkbookOut) GetArtifactIdOk() (*string, bool)`

GetArtifactIdOk returns a tuple with the ArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactId

`func (o *WorkbookOut) SetArtifactId(v string)`

SetArtifactId sets ArtifactId field to given value.


### GetCellCount

`func (o *WorkbookOut) GetCellCount() int32`

GetCellCount returns the CellCount field if non-nil, zero value otherwise.

### GetCellCountOk

`func (o *WorkbookOut) GetCellCountOk() (*int32, bool)`

GetCellCountOk returns a tuple with the CellCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCellCount

`func (o *WorkbookOut) SetCellCount(v int32)`

SetCellCount sets CellCount field to given value.


### GetEditability

`func (o *WorkbookOut) GetEditability() EditabilityOut`

GetEditability returns the Editability field if non-nil, zero value otherwise.

### GetEditabilityOk

`func (o *WorkbookOut) GetEditabilityOk() (*EditabilityOut, bool)`

GetEditabilityOk returns a tuple with the Editability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEditability

`func (o *WorkbookOut) SetEditability(v EditabilityOut)`

SetEditability sets Editability field to given value.


### GetFormat

`func (o *WorkbookOut) GetFormat() string`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *WorkbookOut) GetFormatOk() (*string, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *WorkbookOut) SetFormat(v string)`

SetFormat sets Format field to given value.


### GetRevision

`func (o *WorkbookOut) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *WorkbookOut) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *WorkbookOut) SetRevision(v string)`

SetRevision sets Revision field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
