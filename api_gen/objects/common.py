from api_gen.objects.config import INDENT_WIDTH, INDENT_CHAR


__all__ = ["make_indent"]


def make_indent(level: int) -> str:
    return (INDENT_WIDTH * level) * INDENT_CHAR
