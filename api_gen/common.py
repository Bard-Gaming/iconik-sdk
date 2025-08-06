from typing import Type


def type_name(value: Type) -> str:
    # Note:
    # Some 'types' like the None instance
    # don't define __name__, so set 'str(value)'
    # as the fallback
    return getattr(value, "__name__", str(value))