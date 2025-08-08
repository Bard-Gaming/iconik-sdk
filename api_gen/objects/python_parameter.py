from inspect import Parameter, _empty
from typing import Self


__all__ = ["PythonParameter"]


class PythonParameter:
    def __init__(self, name: str, type: str | None, default_value: str | None) -> None:
        self.name = name
        self.type = type
        self.default_value = default_value

        type_part = f": {self.type}" if self.type is not None else ""
        default_value_part = f" = {self.default_value}" if self.default_value is not None else ""

        self._code = f"{self.name}{type_part}{default_value_part}"

    @classmethod
    def from_signature_parameter(cls, param: Parameter) -> Self:
        name = str(param.name)
        type = str(param.annotation) if param.annotation is not _empty else None
        default_value = str(param.default) if param.default is not _empty else None

        self = cls(name, type, default_value)
        self._code = str(param)  # param's formatter is superior to ours, so use it

        return self

    def __str__(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return f"<PythonParameter {self.name}>"
