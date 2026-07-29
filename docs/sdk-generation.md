# SDK generation contract

The generated Python, TypeScript, and Go clients derive from
`sdk/openapi.json`, not from a live AgentDrive deployment.

`sdk/openapi.provenance.json` records:

- the AgentDrive repository and exact source commit;
- the handler-generated snapshot path;
- the source snapshot SHA-256;
- the pinned OpenAPI Generator image.

CI reconstructs the handler-generated source snapshot from the committed SDK
contract (replacing only the documented server value), verifies its SHA-256
against that provenance, and requires the recorded generator image to match
`sdk/openapi-generator-image.txt`.

The import changes only the snapshot's deployment-derived `servers` sentinel
to the separately reviewed public SDK default
`https://api.agentdrive.run`. It rejects pre-freeze contracts, non-SDK routes,
missing Bearer authentication, missing operation IDs, and duplicates.

Every API contract change uses two coordinated reviews:

1. AgentDrive changes handlers/tests and commits the reviewed OpenAPI snapshot.
2. This repository imports that exact commit, regenerates all clients, and
   records any generated-client migration notes.

CI regenerates with `openapitools/openapi-generator-cli:v7.24.0`, requires a
clean diff, checks exact operation coverage in all three languages, and runs
their tests. The workflow does not fetch production, commit changes, publish
packages, or deploy anything.

The canonical OpenAPI 3.1 file is unchanged by generation. A tested
generation-only view removes object/array defaults that produce invalid Go and
maps multi-type primitive unions to Go's `interface{}` because Generator 7.24
otherwise emits undefined `AnyOf` helpers. The same view maps a free-form
nullable value to the language's open value type for Go and TypeScript because
their templates otherwise emit undefined serializers. Python consumes the
unmodified union schemas. A final deterministic pass strips generator-owned
trailing whitespace and excess EOF blank lines.

Publishing is a separate, explicit release action. Corrected clients should
receive a version and migration note appropriate to their current stability
promise before Josh approves publication.
