from typing import Callable, Type, Collection
import inspect

from api_gen.common import type_name


__all__ = ["MethodGeneratorParameter", "MethodGenerator", "ReferencedMethodGenerator"]


INDENT_WIDTH = 4


class MethodGeneratorParameter:
    def __init__(self, name: str, value_type: Type = inspect._empty) -> None:
        self.name = name
        self.type = value_type if value_type is not inspect._empty else any  # any is a fnc, so __name__ is defined

    def __str__(self) -> str:
        return f"{self.name}: {type_name(self.type)}"

    def __repr__(self) -> str:
        return f"<parameter {self.name}: {type_name(self.type)}>"


class MethodGenerator:
    def __init__(
            self,
            name: str,
            parameters: Collection[MethodGeneratorParameter],
            return_type: Type,
            body: Collection[str] = ("pass",)
    ) -> None:
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.body = body

    def _generate_prototype(self, indent_level: int) -> str:
        indent_1 = " " * (INDENT_WIDTH * indent_level)
        indent_2 = " " * (INDENT_WIDTH * (indent_level + 1))

        params = ",\n".join(f"{indent_2}{param}" for param in self.parameters)

        return (
            f"{indent_1}def {self.name}(\n"
            f"{indent_2}self,\n"
            f"{params}\n"
            f"{indent_1}) -> {type_name(self.return_type)}:\n"
        )

    def _generate_body(self, indent_level: int) -> str:
        indent = " " * (INDENT_WIDTH * indent_level)
        return "\n".join(f"{indent}{line}" for line in self.body)

    def generate(self, indent_level: int = 1) -> str:
        return (
            self._generate_prototype(indent_level) +
            self._generate_body(indent_level + 1)
        )

    def __repr__(self) -> str:
        return f"<method {self.name}: ({', '.join(map(str, self.parameters))}) -> {type_name(self.return_type)}"


class ReferencedMethodGenerator(MethodGenerator):
    def __init__(self, name: str, reference: Callable):
        self.reference = reference

        signature = inspect.signature(reference)

        parameters = self._transform_parameters([
            MethodGeneratorParameter(param.name, param.annotation)
            for param in signature.parameters.values()
        ])

        return_type = signature.return_annotation

        super().__init__(
            name,
            parameters,
            return_type,
            self._build_body_from_reference(parameters)
        )

    def _transform_parameters(
            self,
            parameters: Collection[MethodGeneratorParameter]
    ) -> Collection[MethodGeneratorParameter]:
        """
        This method exists to allow subclasses to transform the parameters
        """
        return parameters

    def _build_body_from_reference(self, parameters: Collection[MethodGeneratorParameter]) -> Collection[str]:
        arguments = ', '.join(param.name for param in parameters)
        return (
            f"return {self.original_name}({arguments})",
        )

    @property
    def original_name(self) -> str:
        return self.reference.__name__
