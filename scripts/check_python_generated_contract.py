"""Fail unless both generated Python clients exactly represent the SDK contract."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from scripts.openapi_sdk_contract import ContractError, load_document, operation_map
    from scripts.python_generated_surface import (
        check_surface_against_contract,
        check_sync_async_parity,
        parse_surface,
        public_operation_names,
    )
except ModuleNotFoundError:  # direct `python scripts/...py` execution
    from openapi_sdk_contract import ContractError, load_document, operation_map
    from python_generated_surface import (
        check_surface_against_contract,
        check_sync_async_parity,
        parse_surface,
        public_operation_names,
    )

DEFAULT_CONTRACT = Path("sdk/openapi.json")
DEFAULT_SYNC_API = Path("sdk/python/src/agentdrive_sdk/generated/sync/api")
DEFAULT_ASYNC_API = Path("sdk/python/src/agentdrive_sdk/generated/async_client/api")


def validate_generated_contract(
    contract_path: Path,
    sync_api: Path,
    async_api: Path,
) -> tuple[dict[str, dict], dict[str, dict]]:
    document = load_document(contract_path)
    operation_ids = set(operation_map(document))
    failures: list[str] = []

    for label, api_root in (("sync", sync_api), ("async", async_api)):
        if not api_root.is_dir():
            failures.append(f"{label}: generated API directory is missing: {api_root}")
            continue
        public = public_operation_names(api_root)
        if public != operation_ids:
            failures.append(
                f"{label}: public operation set differs; "
                f"missing={sorted(operation_ids - public)}, extra={sorted(public - operation_ids)}"
            )
    if failures:
        raise ContractError("\n".join(failures))

    sync = parse_surface(sync_api, operation_ids, expected_async=False)
    async_client = parse_surface(async_api, operation_ids, expected_async=True)
    failures.extend(check_surface_against_contract(document, sync, label="sync"))
    failures.extend(check_surface_against_contract(document, async_client, label="async"))
    failures.extend(check_sync_async_parity(sync, async_client))
    if failures:
        raise ContractError("\n".join(failures))
    return sync, async_client


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--sync-api", type=Path, default=DEFAULT_SYNC_API)
    parser.add_argument("--async-api", type=Path, default=DEFAULT_ASYNC_API)
    args = parser.parse_args()

    try:
        sync, _async_client = validate_generated_contract(
            args.contract, args.sync_api, args.async_api
        )
    except (ContractError, OSError, SyntaxError) as exc:
        print(f"Generated Python contract gate failed:\n{exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    print(
        "Generated Python contract is exact: "
        f"{len(sync)} operations, sync/async callable parity, parameters, request media, "
        "responses, status codes, auth, and response-header transport."
    )


if __name__ == "__main__":
    main()
