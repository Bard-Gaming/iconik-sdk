from typing import Collection
import logging

from api_gen.class_generator import ClassGenerator


__all__ = ["FileGenerator", "FileGeneratorImport"]


LOGGER = logging.getLogger("file_generator")


class FileGeneratorImport:
    def __init__(self, module: str, symbols: Collection[str] | None = None) -> None:
        self.module = module
        self.symbols = symbols

    def __str__(self) -> str:
        return (
            f"from {self.module} import {', '.join(self.symbols)}"
            if self.symbols is not None else
            f"import {self.module}"
        )

    def __repr__(self) -> str:
        return f"<module import {self.module}>"


class FileGenerator:
    def __init__(
            self,
            name: str,
            imports: Collection[FileGeneratorImport],
            file_class: ClassGenerator
    ) -> None:
        self.name = name if name.endswith(".py") else f"{name}.py"
        self.imports = imports
        self.file_class = file_class

    def generate(self, parent_dir: str) -> None:
        path = f"{parent_dir.rstrip('/')}/{self.name.lstrip('/')}"
        LOGGER.info(f"Generating file {path !r}")

        with open(path, "xt") as file:
            file.write(self._generate_imports() + "\n\n")
            file.write(self.file_class.generate())

    def _generate_imports(self) -> str:
        return "\n".join(map(str, self.imports))

    def __repr__(self) -> str:
        return f"<file {self.name}>"
