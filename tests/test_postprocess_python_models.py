from __future__ import annotations

import unittest

from scripts.postprocess_python_models import transform_model


REQUEST_MODEL = '''\
from typing import Any, ClassVar, Dict, Optional, Self
from pydantic import BaseModel, ConfigDict, field_validator

class CreateIn(BaseModel):
    name: str
    role: str
    additional_properties: Dict[str, Any] = {}
    model_config = ConfigDict(validate_assignment=True)

    @field_validator("role")
    def role_validate_enum(cls, value):
        if value not in {"reader"}:
            raise ValueError("bad role")
        return value

    def to_dict(self) -> Dict[str, Any]:
        result = self.model_dump()
        result.update(self.additional_properties)
        return result

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        known = {"name": obj.get("name"), "role": obj.get("role")}
        instance = cls.model_validate(known)
        for key, value in obj.items():
            if key not in known:
                instance.additional_properties[key] = value
        return instance
'''

RESPONSE_MODEL = '''\
from pydantic import BaseModel, ConfigDict, field_validator

class ActorOut(BaseModel):
    type: str
    model_config = ConfigDict(validate_assignment=True)

    @field_validator("type")
    def type_validate_enum(cls, value):
        if value not in {"user"}:
            raise ValueError("bad type")
        return value
'''


class PostprocessPythonModelsTest(unittest.TestCase):
    def test_request_models_forbid_extras_preserve_enums_and_wire_dump_semantics(self):
        transformed = transform_model(REQUEST_MODEL, request_model=True)

        self.assertIn('extra="forbid"', transformed)
        self.assertNotIn("additional_properties: Dict", transformed)
        self.assertIn("def role_validate_enum", transformed)
        self.assertIn("return cls.model_validate(obj)", transformed)
        self.assertIn("exclude_unset=True", transformed)
        self.assertIn("by_alias=True", transformed)

    def test_response_models_ignore_additive_fields_and_open_enum_values(self):
        transformed = transform_model(RESPONSE_MODEL, request_model=False)

        self.assertIn('extra="ignore"', transformed)
        self.assertNotIn("type_validate_enum", transformed)

    def test_transform_is_idempotent(self):
        once = transform_model(REQUEST_MODEL, request_model=True)
        twice = transform_model(once, request_model=True)
        self.assertEqual(once, twice)

    def test_nonnullable_optional_wire_field_rejects_explicit_null_but_stays_omittable(self):
        transformed = transform_model(
            REQUEST_MODEL.replace("name: str", "name: Optional[str] = None"),
            request_model=True,
            nonnullable_fields={"name"},
        )

        self.assertIn("name: str = None", transformed)
        self.assertNotIn("name: Optional[str]", transformed)

    def test_nonnullable_field_keeps_nullable_array_items(self):
        source = REQUEST_MODEL.replace(
            "name: str", "name: Optional[List[Optional[str]]] = None"
        ).replace(
            "from typing import Any, ClassVar, Dict, Optional, Self",
            "from typing import Any, ClassVar, Dict, List, Optional, Self",
        )
        transformed = transform_model(
            source,
            request_model=True,
            nonnullable_fields={"name"},
        )

        self.assertIn("name: List[Optional[str]] = None", transformed)


if __name__ == "__main__":
    unittest.main()
