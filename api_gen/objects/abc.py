import abc


__all__ = ["GeneratorObject"]

INDENT_WIDTH: int = 4


class GeneratorObject(abc.ABC):
    @abc.abstractmethod
    def add(self, other: "GeneratorObject") -> None:
        """
        Adds an object to the contents of the instance.
        All objects can contain other objects.

        For instance, a class may contain methods within
        its body, but it may also contain another class.
        """
        pass

    @abc.abstractmethod
    def dump_bytes(self, level: int = 0) -> bytes:
        """
        The level parameter specifies the level of
        indentation the bytes should be generated
        with.

        This method returns the bytes that should be
        written to a file in order to create the object.

        These bytes should always be able to be decoded
        into UTF-8, since this is how content will be
        generated.
        """
        pass

    def __iadd__(self, other: "GeneratorObject") -> None:
        return self.add(other)

    def __bytes__(self) -> bytes:
        return self.dump_bytes()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"
