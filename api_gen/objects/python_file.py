from typing import Iterable

from api_gen.objects import GeneratorObject


class PythonFile:
    """
    Class that represents a Python file with
    its contents.

    Note: This class doesn't inherit from GeneratorObject,
    as this would mean it can be contained within other
    GeneratorContainerObjects. Alas, a Python file can
    hardly be contained within a class, function, or
    any other type of object, hence the reason it isn't
    a GeneratorObject.
    However, its methods are kept similar to the ones
    from GeneratorObjects, so as to make them easier
    to use.
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


if __name__ == '__main__':
    from api_gen.objects import *

    a = PythonFile()

    a.add_import("typing", "*")
    b = PythonClass("IconikApi")
    b.add_attribute("app_id", "str")
    b.add_attribute("auth_token", "str")
    a.add(b)

    print(a.dump_bytes().decode("utf-8"))
