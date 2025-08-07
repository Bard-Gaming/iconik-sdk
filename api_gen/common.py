from typing import Type


def type_name(value: Type | None) -> str:
    # None is an instance of NoneType, which doesn't
    # define __module__ (as well as not being what we want),
    # so return "None" instead.
    if value is None:
        return str(value)

    # Typing's classes all have exactly what we
    # want within their __str__ method, so use it:
    if value.__module__ == "typing":
        return str(value)

    if value.__module__ == 'builtins':
        return getattr(value, "__name__", str(value))

    return f"{value.__module__}.{value.__name__}"


if __name__ == '__main__':
    from pydantic.fields import FieldInfo
    from pydantic import Strict
    from typing import Collection

    print(type_name(FieldInfo))
    print(type_name(Collection[Strict(strict=False)]))
    print(type_name(str))
    print(type_name(None))
