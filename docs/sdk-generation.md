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
their tests. Before generation it compares the candidate OpenAPI document with
the PR/push base and rejects breaking operation, parameter, request, response,
status, media, header, authentication, or server changes. The workflow does
not fetch production, commit changes, publish packages, or deploy anything.

The canonical OpenAPI 3.1 file is unchanged by generation. A tested
generation-only view removes object/array defaults that produce invalid Go and
maps multi-type primitive unions to Go's `interface{}` because Generator 7.24
otherwise emits undefined `AnyOf` helpers. The same view maps a free-form
nullable value to the language's open value type for Go and TypeScript because
their templates otherwise emit undefined serializers. Python consumes the
unmodified union schemas. A final deterministic pass strips generator-owned
trailing whitespace and excess EOF blank lines.

## Python generated-core gates

Python generation produces two independent clients:

- `sdk/python/src/agentdrive_sdk/generated/sync` (`urllib3`);
- `sdk/python/src/agentdrive_sdk/generated/async_client` (`httpx`, async only).

`check_python_generated_contract.py` parses both source trees. It requires all
three public variants for every operation, exact sync/async parameter and
docstring parity, and contract-matching HTTP methods, paths, authentication,
wire parameter names/locations/requiredness/types, request media, response
media/status/model maps, and a response-header carrier.

`generate_python_contract_manifest.py --check` provides the deeper review
gate. Its committed manifest hashes every constraint-bearing component schema
and generated model class while directly comparing each component's property
set, requiredness, and nullability. For every response it records exact status,
media, and header names/schema hashes. Generated Python does not create one
attribute per header: both clients copy the complete raw header mapping into
`ApiResponse.headers`; the manifest verifies that carrier and forwarding path.

`postprocess_python_models.py` applies the compatibility policy that OpenAPI
Generator does not express correctly by itself:

- request models reject unknown fields and retain closed enum validation;
- optional-but-non-nullable fields remain omittable but reject explicit null;
- response models ignore additive fields and accept future enum strings;
- PATCH request serialization preserves explicit null while omitting unset
  fields.

`generate_python_api_reference.py` parses the committed source rather than
guessing from OpenAPI alone. Its checked output includes exact sync/async
callable signatures, all variants and generated docstrings, plus the wire
request/response tables. Response tables pair each OpenAPI schema with its
generated Python type, and anonymous request/error objects link to recursively
rendered inline field definitions instead of opaque schema hashes.

## Intentional Phase 1 compatibility reset

The pre-Phase 1 `0.0.1` contract exposed 110 operations, including browser and
internal routes that were never a supported SDK surface. The Phase 1 contract
intentionally replaces it with the reviewed 42-operation SDK contract. The
single transition is authorized only by
`sdk/openapi.compatibility-reset.json`, whose exact old digest, new digest, and
AgentDrive source commit must all match. It is not a skip flag: any further
change to either document invalidates it. Once the 42-operation contract is the
base branch, normal directional compatibility comparison applies.

Publishing is a separate, explicit release action. A manual dispatch fails
unless it runs from `refs/heads/main`; a GitHub release commit must be contained
in `origin/main`. The publish workflow then calls the same reusable acceptance
workflow as pull requests: unit/provenance/compatibility checks, pinned
regeneration and freshness, exact Python shape/model/reference gates,
conformance and package builds, TypeScript build, and Go tests must all pass on
the release commit. Only then does release integrity require the release tag
(`vX.Y.Z`) or manual input to match `sdk/SDK_VERSION`, Python root and generated
versions, and TypeScript package/lock versions. PyPI, npm, and Go tag jobs
depend on those gates and fail rather than silently accepting an
already-published immutable version. Trusted-publisher ownership/OIDC must be
verified after the GitHub repository transfer before approving the first
`0.1.0` publish.
