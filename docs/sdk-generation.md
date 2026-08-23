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
`https://drive.tokencanopy.com`. It rejects pre-freeze contracts, non-SDK routes,
missing Bearer authentication, missing operation IDs, and duplicates.

Every API contract change uses two coordinated reviews:

1. AgentDrive changes handlers/tests and commits the reviewed OpenAPI snapshot.
2. This repository imports that exact commit, regenerates all clients, and
   records any generated-client migration notes.

CI regenerates with the OpenAPI Generator 7.16.0 image pinned to the immutable
digest in `sdk/openapi-generator-image.txt`, requires a clean diff, checks exact
operation coverage in all three languages, and runs their tests. The workflow
does not fetch production, commit changes, publish packages, or deploy
anything.

The source repository is private, so public SDK CI cannot independently fetch
`source_repository@source_commit`. The recorded source commit and digest are
therefore an operator-reviewed cross-repository attestation; the checker
verifies the committed contract's exact canonical serialization and rejects
stale or self-inconsistent metadata.

The canonical OpenAPI 3.1 file is unchanged by generation. Tested
generation-only views downgrade the document to OpenAPI 3.0.3, convert 3.1
nullable and `const` forms, and remove object/array defaults that produce
invalid Go. They map multi-type primitive unions to Go's `interface{}` because
the pinned generator otherwise emits undefined `AnyOf` helpers. The same views
map free-form nullable values to the language's open value type for Go and
TypeScript. A small tested post-generation compatibility pass qualifies the
TypeScript generator's free-form multipart `objectToJSON` call and provides an
identity serializer. A final deterministic pass strips generator-owned trailing
whitespace and excess EOF blank lines.

Publishing is a separate, explicit release action. Corrected clients should
receive a version and migration note appropriate to their current stability
promise before Josh approves publication.
