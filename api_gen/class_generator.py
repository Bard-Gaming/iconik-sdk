from typing import Type
from api_gen.method_generator import MethodGenerator


class ClassGeneratorAttribute:
    def __init__(self, name: str, value_type: Type) -> None:
        self.name = name
        self.type = value_type

    def __str__(self) -> str:
        return f"{self.name}: {self.type.__name__}"

    def __repr__(self) -> str:
        return f"<attribute {self.name}: {self.type.__name__}>"


class ClassGenerator:
    def __init__(
            self,
            name: str,
            attributes: tuple[ClassGeneratorAttribute, ...],
            methods: tuple[MethodGenerator]
    ) -> None:
        self.name = name
        self.attributes = attributes
        self.methods = methods

    def generate(self, file_path: str) -> None:
        with open(file_path, "wt") as file:
            file.write(self._generate_header())
            file.write(self._generate_methods())
            file.write(self._generate_footer())

    def _generate_header(self) -> str:
        return (
            f"class {self.name}:\n"
            f"    \"\"\"\n"
            f"    Class generated using {self.__module__.split('.')[0]}.\n"
            f"    \"\"\"\n"
            f"    def __init__(\n"
            f"        self,\n"
            f"{',\n'.join(f'        {param}'for param in self.attributes)}\n"
            f"    ) -> None:\n"
            f"{'\n'.join(f'        self.{attrib} = {attrib.name}' for attrib in self.attributes)}\n"
            f"\n"
        )

    def _generate_methods(self) -> str:
        return "".join(method.generate() for method in self.methods)

    def _generate_footer(self) -> str:
        return (
            f"    def __repr__(self) -> str:\n"
             "        return f'{self.__class__.__name__}(" f"{', '.join('{' f'self.{attrib.name} !r' '}' for attrib in self.attributes )}" ")'"
            f"\n"
        )

    def __repr__(self) -> str:
        return f"ClassGenerator({self.name !r})"
