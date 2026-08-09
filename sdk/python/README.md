# AgentDrive Python SDK

`agentdrive-sdk` is the official typed Python client for the AgentDrive REST
API. Version `0.1.0` contains the Phase 1 generated core: complete synchronous
and asynchronous clients for all 42 operations in the reviewed OpenAPI
contract. The ergonomic resource facade is a later phase.

> Alpha software: the old `0.0.1` distribution predates this contract and is
> superseded. Phase 1 begins at `0.1.0`; this repository change does not itself
> publish that release. Generated operation names and models mirror the OpenAPI
> contract exactly.

## Install

```bash
python -m pip install agentdrive-sdk
```

## Synchronous client

```python
import os

from agentdrive_sdk.generated.sync import ApiClient, Configuration, DrivesApi

configuration = Configuration(
    host="https://api.agentdrive.run",
    access_token=os.environ["AGENTDRIVE_API_KEY"],
)

with ApiClient(configuration) as api_client:
    drives = DrivesApi(api_client)
    page = drives.drives_list()
    print(page)
```

## Asynchronous client

```python
import os

from agentdrive_sdk.generated.async_client import (
    ApiClient,
    Configuration,
    DrivesApi,
)


async def list_drives():
    configuration = Configuration(
        host="https://api.agentdrive.run",
        access_token=os.environ["AGENTDRIVE_API_KEY"],
    )
    async with ApiClient(configuration) as api_client:
        drives = DrivesApi(api_client)
        return await drives.drives_list()
```

Both clients also expose `*_with_http_info` and
`*_without_preload_content` variants for status, headers, streaming, and other
low-level response handling. Automatic redirects are disabled in both
transports so an AgentDrive bearer token is never forwarded to a signed-storage
or share host. Callers must inspect and follow an allowed redirect explicitly
without the authorization header.

The complete generated API-class signatures, docstrings, parameters, request
media, response status/model map, and declared response headers are in the
[generated API reference](https://github.com/tokencanopy/agentdrive-sdk/blob/main/docs/python-sdk-api-reference.md).

## Generated-code boundary

Only these directories are generated:

- `src/agentdrive_sdk/generated/sync`
- `src/agentdrive_sdk/generated/async_client`

Do not edit them manually. Regenerate them from the repository root with:

```bash
bash scripts/generate-sdks.sh sdk/openapi.json
```

The package metadata, README, license, type marker, tests, and future ergonomic
facade live outside the generated tree and survive regeneration.
