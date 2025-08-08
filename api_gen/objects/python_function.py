from typing import Self, Callable, overload
import inspect

from api_gen.objects import GeneratorObject, GeneratorContainerObject
from api_gen.objects.python_parameter import PythonParameter
from api_gen.objects.common import make_indent


__all__ = ["PythonFunction"]


class PythonFunction(GeneratorContainerObject):
    def __init__(self, name: str) -> None:
        self.name = name
        self._parameters: list[PythonParameter] = []
        self._return_type: str = "any"
        self._contents: list[GeneratorObject] = []

    @classmethod
    def from_reference(cls, function: Callable) -> Self:
        signature = inspect.signature(function)

        self = cls(function.__name__)

        for param in signature.parameters.values():
            self.add_parameter(PythonParameter.from_signature_parameter(param))

        if signature.return_annotation is not inspect._empty:
            self.set_return_type(signature.return_annotation)

        return self

    @overload
    def add_parameter(self, parameter: PythonParameter) -> None:
        pass

    @overload
    def add_parameter(self, name: str, type: str | None = None, default_value: str | None = None) -> None:
        pass

    def add_parameter(
            self,
            determinant: PythonParameter | str,
            ptype: str | None = None,
            default_value: str | None = None
    ) -> None:
        if isinstance(determinant, PythonParameter):
            self._parameters.append(determinant)
            return

        parameter = PythonParameter(determinant, ptype, default_value)
        self.remove_parameter(determinant)  # remove parameter in case it already exists
        self._parameters.append(parameter)

    def remove_parameter(self, name: str) -> bool:
        for i in range(len(self._parameters)):
            if self._parameters[i].name == name:
                del self._parameters[i]
                return True

        return False

    def set_return_type(self, type: str) -> None:
        self._return_type = type

    def add(self, other: "GeneratorObject") -> None:
        self._contents.append(other)

    def _generate_params(self, indent: str) -> tuple[str, ...]:
        return tuple(
            f"{indent}{self._parameters[i]}" + ("," if i != len(self._parameters) - 1 else "")
            for i in range(len(self._parameters))
        )

    def _generate_header(self, level: int) -> bytes:
        indent = make_indent(1)

        object_type = self.__class__.__name__.removeprefix("Python")

        header = (
            f"def {self.name}(",
            *self._generate_params(indent),
            f") -> {self._return_type}:",
            f"{indent}\"\"\"",
            f"{indent}{object_type} generated using the {self.__module__.split('.')[0]} library.",
            f"{indent}\"\"\"",
        )

        # indent everything by <level> levels and add newlines:
        header = "".join(f"{make_indent(level)}{line}\n" for line in header)
        return header.encode("utf-8")

    def dump_bytes(self, level: int = 0) -> bytes:
        result = self._generate_header(level)

        if self._contents:
            result += b"\n".join(obj.dump_bytes(level + 1) for obj in self._contents)
        else:
            result += f"{make_indent(level + 1)}pass\n".encode("utf-8")

        return result
