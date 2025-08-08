from typing import Iterable

from api_gen.objects import GeneratorObject


class PythonFile:
    """
    The object representation of a python file.

    Note: This class isn't a GeneratorObject, as
    a Python File can't contain a Python File in
    itself. It is, however, aimed at being used
    in a similar fashion to GeneratorObjects,
    purely for ease of use.
    """

    def __init__(self) -> None:
        self._imports: list[str] = []
        self._contents: list[GeneratorObject] = []

    def add_import(self, module: str, symbols: Iterable[str] | str | None = None):
        if symbols is None:
            import_stmt = f"import {module}"
        elif isinstance(symbols, str):
            import_stmt = f"from {module} import {symbols}"
        else:
            import_stmt = f"from {module} import {', '.join(symbols)}"

        self._imports.append(f"{import_stmt}\n")

    def add(self, obj: GeneratorObject):
        self._contents.append(obj)

    def dump_bytes(self) -> bytes:
        separator = b"\n\n"

        result = b"".join(
            import_stmt.encode("utf-8")
            for import_stmt in self._imports
        )

        if self._imports:
            result += separator

        result += separator.join(
            obj.dump_bytes()
            for obj in self._contents
        )

        return result + b"\n"  # end with newline for unix :>

    def __bytes__(self) -> bytes:
        return self.dump_bytes()

    def __repr__(self) -> str:
        return "<PythonFile>"
