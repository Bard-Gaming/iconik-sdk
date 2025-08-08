from api_gen.objects.abc import GeneratorObject, GeneratorContainerObject
from api_gen.objects.common import make_indent


__all__ = ["PythonClass"]


class PythonClass(GeneratorContainerObject):
    def __init__(self, name: str):
        self.name = name
        self._attributes: list[tuple[str, str | None, str | None]] = []
        self._contents: list[GeneratorObject] = []

    def add(self, other: "GeneratorObject") -> None:
        self._contents.append(other)

    def add_attribute(self, name: str, type: str = None, default_value: str = None) -> None:
        self._attributes.append((name, type, default_value))

    def _generate_init(self) -> None:
        init_method = None  # TODO: Implement
        self._contents.insert(0, init_method)

    def _generate_header(self, level: int) -> bytes:
        indent = make_indent(1)

        header = (
            f"class {self.name}:",
            f"{indent}\"\"\"",
            f"{indent}Class generated using the {self.__module__.split('.')[0]} library.",
            f"{indent}\"\"\"",
        )

        # indent everything by <level> levels and add newlines:
        header = "".join(f"{make_indent(level)}{line}\n" for line in header)

        return header.encode("utf-8")

    def dump_bytes(self, level: int = 0) -> bytes:
        result = self._generate_header(level) + b"\n"

        self._generate_init()

        result += b"\n".join(obj.dump_bytes(level + 1) for obj in self._contents)

        return result
