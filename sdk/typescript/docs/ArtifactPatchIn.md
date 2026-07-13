
# ArtifactPatchIn

PATCH /v0/artifacts/{art_id} body — metadata-only partial (JSON-merge-patch) update.  Every field is optional. Presence is what matters, not the value: a field left out of the body (per Pydantic `model_fields_set`) is left unchanged; a field that IS present is applied — with an explicit `null` / `[]` / `{}` meaning \"clear it\". This mirrors the MCP `set_metadata` tool and the core `patch_artifact_metadata` sentinel semantics (omitted = preserve, present = replace/clear).    * `labels`   — replace the label set; `[]` or `null` clears it.   * `metadata` — replace the free-form metadata object; `{}` or `null`                  clears it.   * `source`   — replace provenance refs; `null` (or `{\"refs\": []}`)                  clears them.  PATCH is metadata-only: to move/rename an artifact, use `POST /v0/artifacts/{art_id}/move`. `extra=\"forbid\"` makes a stray field (notably a legacy `path`) a hard 422 rather than a silent no-op — a clean-break signal to migrate to the move verb.

## Properties

Name | Type
------------ | -------------
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: any; }
`source` | [ArtifactSource](ArtifactSource.md)

## Example

```typescript
import type { ArtifactPatchIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "labels": null,
  "metadata": null,
  "source": null,
} satisfies ArtifactPatchIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactPatchIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


