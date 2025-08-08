from api_gen.objects.common import make_indent
from api_gen.objects import GeneratorObject


__all__ = ["PythonStatement"]


class PythonStatement(GeneratorObject):
    def __init__(self, line: str) -> None:
        self.line = line

    def dump_bytes(self, level: int = 0) -> bytes:
        return f"{make_indent(level)}{self.line}".encode("utf-8")
