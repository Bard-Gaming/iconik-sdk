import abc


__all__ = ["GeneratorObject", "GeneratorContainerObject"]

INDENT_WIDTH: int = 4


class GeneratorObject(abc.ABC):
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

    def __bytes__(self) -> bytes:
        return self.dump_bytes()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class GeneratorContainerObject(GeneratorObject):
    @abc.abstractmethod
    def add(self, other: GeneratorObject) -> None:
        """
        Adds an object to the contents of the instance.
        This object can also be a GeneratorContainerObject.

        For instance, a class may contain methods within
        its body, but it may also contain another class.
        """
        pass

    def __iadd__(self, other: GeneratorObject) -> None:
        return self.add(other)
