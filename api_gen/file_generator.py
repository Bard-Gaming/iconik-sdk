from pathlib import Path
import logging
import abc
import os

from api_gen.iconik.utils import transform_case


__all__ = ["FileGenerator", "ApiFileGenerator"]


class FileGenerator(abc.ABC):
    def __init__(self, name: str = None) -> None:
        self.name = name if name is not None else transform_case(self.__class__.__name__, "SNAKE_CASE")
        self._logger = logging.getLogger(self.name)

    @abc.abstractmethod
    def write(self, rel_path: str, content: str | bytes) -> None:
        self._logger.info(f"writing content of type {content.__class__.__name__ !r} to {rel_path !r}")

    @abc.abstractmethod
    def generate(self, directory: str) -> None:
        self._logger.info(f"generating content to directory {directory !r}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class ApiFileGenerator(FileGenerator):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)

        self._content_table: dict[str, bytes] = {}

    def write(self, rel_path: str, content: str | bytes) -> None:
        super().write(rel_path, content)
        rel_path = str(Path(rel_path))  # validate path

        # Me when not allowed to 'getattr(self, f"_write_{content.__class__.__name__}", self._unsupported_write)':
        # o(TヘTo) -> (╯_╰)

        if isinstance(content, str):
            self._write_str(rel_path, content)
            return  # 'return None' is not the same as 'return' for Pycharm...
        elif isinstance(content, bytes):
            self._write_bytes(rel_path, content)
            return

        self._unsupported_write(rel_path, content)

    def generate(self, directory: str) -> None:
        super().generate(directory)
        directory = str(Path(directory))

        for path, content in self._content_table.items():
            full_path = f"{directory.rstrip('/')}/{path.lstrip('/')}"

            parent_dir = '/'.join(full_path.strip('/').split('/')[:-1])
            self._mkdir_recursive(parent_dir)

            with open(full_path, "xb") as file:
                file.write(content)

    def _write_bytes(self, rel_path: str, content: bytes) -> None:
        if rel_path in self._content_table:
            self._content_table[rel_path] += content
        else:
            self._content_table[rel_path] = content

    def _write_str(self, rel_path: str, content: str) -> None:
        data = content.encode("utf-8")
        self._write_bytes(rel_path, data)

    def _unsupported_write(self, rel_path: str, content: str) -> str:
        cls_name = content.__class__.__name__

        self._logger.error(f"unsupported write to {rel_path !r} with type {cls_name !r}")

        raise TypeError(
            f"Unsupported write operation with value of type {cls_name !r}"
        )

    @staticmethod
    def _mkdir_safe(directory: str) -> None:
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass  # this is fine; other errors aren't.

    def _mkdir_recursive(self, path: str) -> None:
        directories = path.strip('/').split('/')

        for dir_span in range(1, len(directories) + 1):
            path = '/'.join(directories[:dir_span])
            self._mkdir_safe(path)
