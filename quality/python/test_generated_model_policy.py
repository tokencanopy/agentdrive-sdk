from __future__ import annotations

import importlib
from pathlib import Path

import pytest
from pydantic import ValidationError

from scripts.openapi_sdk_contract import load_document, model_contexts, python_name

NAMESPACES = (
    "agentdrive_sdk.generated.sync",
    "agentdrive_sdk.generated.async_client",
)


def _model(namespace: str, name: str):
    module = importlib.import_module(f"{namespace}.models.{python_name(name)}")
    return getattr(module, name)


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_all_contract_models_have_directional_extra_field_policy(namespace: str):
    contract = load_document(Path("sdk/openapi.json"))
    request_models, response_models = model_contexts(contract)

    for name in sorted(request_models):
        model = _model(namespace, name)
        assert model.model_config.get("extra") == "forbid", name
        assert "additional_properties" not in model.model_fields, name
    for name in sorted(response_models):
        model = _model(namespace, name)
        assert model.model_config.get("extra") == "ignore", name


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_additive_response_field_and_unknown_response_enum_are_accepted(namespace: str):
    actor = _model(namespace, "ChangeActorOut").from_dict(
        {"id": None, "type": "future_actor", "future_field": {"nested": True}}
    )

    assert actor.type == "future_actor"
    assert actor.id is None
    assert not hasattr(actor, "future_field")


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_request_models_reject_unknown_fields_through_both_entry_points(namespace: str):
    drive_create = _model(namespace, "DriveCreateIn")
    payload = {"name": "research", "future_field": True}

    with pytest.raises(ValidationError):
        drive_create.model_validate(payload)
    with pytest.raises(ValidationError):
        drive_create.from_dict(payload)


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_optional_nonnullable_request_field_rejects_explicit_null(namespace: str):
    drive_create = _model(namespace, "DriveCreateIn")

    assert drive_create.model_validate({"name": "research"}).metadata is None
    with pytest.raises(ValidationError):
        drive_create.model_validate({"name": "research", "metadata": None})


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_request_enum_remains_closed(namespace: str):
    grant_create = _model(namespace, "GrantCreateIn")

    with pytest.raises(ValidationError):
        grant_create.from_dict(
            {
                "principal_type": "agent",
                "resource_id": "drv_0123456789abcdef",
                "resource_type": "drive",
                "role": "future_role",
            }
        )


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_patch_dump_distinguishes_explicit_null_from_unset(namespace: str):
    grant_update = _model(namespace, "GrantUpdateIn")

    assert grant_update(expires_at=None).to_dict() == {"expires_at": None}
    assert grant_update().to_dict() == {}
