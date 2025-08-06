from simple_api_generator.method_generator import MethodGenerator

class ClassGenerator:
    def __init__(self, name: str, attributes: tuple[str], methods: tuple[MethodGenerator]) -> None:
        self.name = name
        self.attributes = attributes
        self.methods = methods

    def _generate_header(self) -> str:
        init_params = ("self",) + self.attributes

        return (
            f"class {self.name}:\n"
            f"    def __init__(\n"
            f"{',\n'.join(f'        {param}'for param in init_params)}\n"
            f"    ) -> None:\n"
            f"        pass\n"
        )

    def __repr__(self) -> str:
        return f"ClassGenerator({self.name !r})"

a = ClassGenerator("CoolClass", ("a", "b"), (None,))
print(a._generate_header())
