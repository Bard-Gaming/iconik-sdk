from api_gen.objects import GeneratorObject, GeneratorContainerObject
from api_gen.objects.python_parameter import PythonParameter
from api_gen.objects.common import make_indent


class PythonFunction(GeneratorContainerObject):
    def __init__(self, name: str) -> None:
        self.name = name
        self._parameters: list[PythonParameter] = []
        self._return_type: str = "None"
        self._contents: list[GeneratorObject] = []

    def add_parameter(self, name: str, type: str | None = None, default_value: str | None = None) -> None:
        parameter = PythonParameter(name, type, default_value)
        self.remove_parameter(name)  # remove parameter in case it already exists
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

        header = (
            f"def {self.name}(",
            *self._generate_params(indent),
            f") -> {self._return_type}:",
            f"{indent}\"\"\"",
            f"{indent}Function generated using the {self.__module__.split('.')[0]} library.",
            f"{indent}\"\"\"",
        )

        # indent everything by <level> levels and add newlines:
        header = "".join(f"{make_indent(level)}{line}\n" for line in header)
        return header.encode("utf-8")

    def dump_bytes(self, level: int = 0) -> bytes:
        result = self._generate_header(level)

        result += b"\n".join(obj.dump_bytes(level + 1) for obj in self._contents)

        return result
