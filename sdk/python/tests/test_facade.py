from __future__ import annotations

from types import SimpleNamespace

import pytest

from agentdrive_sdk import (
    AgentDriveClient,
    AccessToken,
    CallableTokenProvider,
    InvalidPathError,
    PreconditionFailedError,
    StaticTokenProvider,
)
from agentdrive_sdk.generated.exceptions import ApiException


DRIVE_ID = "drv_0000000000000001"
ROOT_FOLDER_ID = "fld_0000000000000001"
FOLDER_ID = "fld_0000000000000002"
ARTIFACT_ID = "art_0000000000000001"


def response(data, status_code=200, headers=None):
    return SimpleNamespace(data=data, status_code=status_code, headers=headers or {})


def test_synthetic_sdk_journey_uses_ids_revisions_and_cursor_pages():
    client = AgentDriveClient(token_provider=StaticTokenProvider("synthetic-token"))
    calls = []

    def drives_create(**kwargs):
        calls.append(("drives_create", kwargs))
        return response(SimpleNamespace(id=DRIVE_ID, root_folder_id=ROOT_FOLDER_ID, revision="drev-1"), 201)

    def folders_create(**kwargs):
        calls.append(("folders_create", kwargs))
        return response(SimpleNamespace(id=FOLDER_ID, parent_id=ROOT_FOLDER_ID, revision="frev-1"), 201)

    def artifacts_create(**kwargs):
        calls.append(("artifacts_create", kwargs))
        return response(SimpleNamespace(id=ARTIFACT_ID, parent_id=FOLDER_ID, revision="arev-1", name="note.txt"), 201)

    def entries_list(**kwargs):
        calls.append(("entries_list", kwargs))
        item = SimpleNamespace(actual_instance=SimpleNamespace(id=ARTIFACT_ID, type="artifact", name="note.txt"))
        cursor = None if kwargs.get("cursor") else "cursor-2"
        return response(SimpleNamespace(entries=[item], next_cursor=cursor))

    def lookup(**kwargs):
        calls.append(("lookup", kwargs))
        return response(SimpleNamespace(id=ARTIFACT_ID, type="artifact", parent_id=FOLDER_ID, revision="arev-1"))

    def artifacts_content(**kwargs):
        calls.append(("artifacts_content", kwargs))
        return response(b"hello synthetic AgentDrive")

    def artifacts_update(**kwargs):
        calls.append(("artifacts_update", kwargs))
        return response(SimpleNamespace(id=ARTIFACT_ID, revision="arev-2", name="renamed.txt"))

    def versions_list(**kwargs):
        calls.append(("versions_list", kwargs))
        return response(SimpleNamespace(items=[SimpleNamespace(id="ver-1")], next_cursor=None))

    def artifacts_delete(**kwargs):
        calls.append(("artifacts_delete", kwargs))
        return response(SimpleNamespace(id=ARTIFACT_ID, state="deleted"))

    client._apis["drives"].drives_create_with_http_info = drives_create
    client._apis["folders"].folders_create_with_http_info = folders_create
    client._apis["artifacts"].artifacts_create_with_http_info = artifacts_create
    client._apis["navigation"].entries_list_with_http_info = entries_list
    client._apis["navigation"].lookup_with_http_info = lookup
    client._apis["artifacts"].artifacts_content_with_http_info = artifacts_content
    client._apis["artifacts"].artifacts_update_with_http_info = artifacts_update
    client._apis["versions"].versions_list_with_http_info = versions_list
    client._apis["artifacts"].artifacts_delete_with_http_info = artifacts_delete

    drive = client.drives.create("Synthetic Drive", idempotency_key="idem-drive")
    folder = client.folders.create(DRIVE_ID, "docs", parent_id=drive.root_folder_id, idempotency_key="idem-folder")
    artifact = client.artifacts.create(
        DRIVE_ID,
        "note.txt",
        content=b"hello synthetic AgentDrive",
        parent_id=folder.id,
        content_type="text/plain",
        idempotency_key="idem-artifact",
    )
    entries = list(client.entries.iter_items(DRIVE_ID, parent_id=folder.id, max_pages=2))
    looked_up = client.entries.lookup(DRIVE_ID, "docs/note.txt", type="artifact")
    content = client.artifacts.content(DRIVE_ID, looked_up.id)
    updated = client.artifacts.update(DRIVE_ID, artifact.id, revision=artifact.revision, name="renamed.txt", idempotency_key="idem-update")
    versions = list(client.versions.iter_items(DRIVE_ID, artifact.id))
    deleted = client.artifacts.delete(DRIVE_ID, updated.id, revision=updated.revision, idempotency_key="idem-delete")

    assert drive.id == DRIVE_ID
    assert folder.id == FOLDER_ID
    assert artifact.id == ARTIFACT_ID
    assert entries[0].id == ARTIFACT_ID
    assert looked_up.id == ARTIFACT_ID
    assert content.startswith(b"hello synthetic")
    assert versions[0].id == "ver-1"
    assert deleted.state == "deleted"

    artifact_call = next(kwargs for name, kwargs in calls if name == "artifacts_create")
    assert artifact_call["idempotency_key"] == "idem-artifact"
    update_call = next(kwargs for name, kwargs in calls if name == "artifacts_update")
    assert update_call["if_match"] == '"arev-1"'
    delete_call = next(kwargs for name, kwargs in calls if name == "artifacts_delete")
    assert delete_call["if_match"] == '"arev-2"'


def test_token_provider_renews_once_after_401_and_keeps_mutation_key():
    tokens = []

    def token(force_refresh):
        tokens.append(force_refresh)
        return AccessToken("new-token" if force_refresh else "old-token")

    client = AgentDriveClient(token_provider=CallableTokenProvider(token))
    attempts = []

    def create(**kwargs):
        attempts.append(kwargs)
        if len(attempts) == 1:
            raise ApiException(status=401, reason="expired")
        return response(SimpleNamespace(id="drv_test"), 201)

    client._apis["drives"].drives_create_with_http_info = create
    created = client.drives.create("Synthetic", idempotency_key="idem-stable")

    assert created.id == "drv_test"
    assert tokens == [False, True, False]
    assert attempts[0]["idempotency_key"] == attempts[1]["idempotency_key"] == "idem-stable"


def test_precondition_error_is_typed_and_path_helpers_reject_unsafe_values(tmp_path):
    client = AgentDriveClient(token_provider=StaticTokenProvider("synthetic-token"))

    def update(**_kwargs):
        raise ApiException(
            status=412,
            reason="stale revision",
            body='{"error":{"code":"STALE_REVISION","message":"revision is stale"}}',
            data=None,
        )

    client._apis["drives"].drives_update_with_http_info = update
    with pytest.raises(PreconditionFailedError) as caught:
        client.drives.update("drv_test", revision="rev-1", name="new")
    assert caught.value.code == "STALE_REVISION"
    assert caught.value.status_code == 412

    with pytest.raises(InvalidPathError):
        client.entries.lookup("drv_test", "../secrets")

    credential = tmp_path / ".env"
    credential.write_text("TOKEN=synthetic", encoding="utf-8")
    with pytest.raises(InvalidPathError):
        list(client.artifacts.upload_directory("drv_test", tmp_path))
