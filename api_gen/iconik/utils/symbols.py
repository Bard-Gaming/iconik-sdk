import abc
from typing import Collection, Type, Self, Literal


__all__ = ["transform_case"]


class CaseSymbol(abc.ABC):
    def __init__(self, value: str):
        self.value = value

    @abc.abstractmethod
    def is_valid(self) -> bool:
        pass

    @abc.abstractmethod
    def to_words(self) -> tuple[str, ...]:
        pass

    @classmethod
    @abc.abstractmethod
    def from_words(cls, words: Collection[str]) -> Self:
        pass

    def to_case(self, case: Type["SnakeCaseSymbol | CamelCaseSymbol"]) -> "CaseSymbol":
        if case is self.__class__:
            return self

        words = self.to_words()
        return case.from_words(words)

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value !r})"


class SnakeCaseSymbol(CaseSymbol):
    def is_valid(self) -> bool:
        return all(
            char.islower() or
            char.isdigit() or
            char == "_"
            for char in self.value
        )

    def to_words(self) -> tuple[str, ...]:
        return tuple(self.value.split("_"))

    @classmethod
    def from_words(cls, words: Collection[str]) -> Self:
        return cls("_".join(word.lower() for word in words))


class CamelCaseSymbol(CaseSymbol):
    def is_valid(self) -> bool:
        # Disallow special characters (such as '_')
        is_alphanum = all(
            char.isalnum()
            for char in self.value
        )

        # At least a single word must be there,
        # so at least 1 uppercase letter is required
        contains_upper = any(
            char.isupper()
            for char in self.value
        )

        return contains_upper and is_alphanum

    def to_words(self) -> tuple[str, ...]:
        words = []

        start = 0
        while start < len(self.value):
            i = start + 1
            while i < len(self.value) and not self.value[i].isupper():
                i += 1
            words.append(self.value[start:i])
            start = i

        return tuple(words)

    @classmethod
    def from_words(cls, words: Collection[str]) -> Self:
        return cls("".join(word.capitalize() for word in words))


SUPPORTED_SYMBOL_CASES = Literal["SNAKE_CASE", "CAMEL_CASE"]

CASE_LOOKUP = {
    "SNAKE_CASE": SnakeCaseSymbol,
    "CAMEL_CASE": CamelCaseSymbol,
}


def determine_symbol_case(symbol: str) -> Type[SnakeCaseSymbol | CamelCaseSymbol]:
    for case in CASE_LOOKUP.values():
        attempt = case(symbol)
        if attempt.is_valid():
            return case

    raise ValueError(f"Symbol {symbol !r} is in no known case")

def transform_case(symbol: str, target_case: SUPPORTED_SYMBOL_CASES) -> str:
    """
    Returns the symbol in the specified case is possible.
    If the symbol isn't in any known case (meaning it can't be transformed),
    the symbol will be returned unchanged.
    """
    try:
        symbol_case = determine_symbol_case(symbol)
    except ValueError:
        return symbol

    target_case_cls = CASE_LOOKUP.get(target_case)
    if target_case_cls is None:
        raise ValueError(
            f"Symbol case {target_case !r} doesn't exist. "
            f"The following are supported: {', '.join(repr(val) for val in CASE_LOOKUP.keys())}"
        )

    return symbol_case(symbol).to_case(target_case_cls).value
