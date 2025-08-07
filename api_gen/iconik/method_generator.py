from typing import Collection, Callable, Self

from api_gen.class_generator import ClassGeneratorAttribute
from api_gen.method_generator import MethodGenerator, MethodGeneratorParameter


__all__ = ["IconikMethodGenerator"]


CATEGORIES = {
    "approvals", "assets", "collections",
    "custom_actions", "playlists", "projects",
    "sequences", "shares", "sync_sessions"
}


class IconikMethodGenerator(MethodGenerator):
    @classmethod
    def from_reference(cls, name: str, reference: Callable) -> Self:
        method = super().from_reference(name, reference)

        method.parameters = tuple(filter(
            # Remove autofilled parameters
            lambda param: param.name[0] != '_' and param.name not in cls._autofilled_parameters,
            method.parameters
        ))

        arguments = (
            ", ".join(f"{param}=self.{param}" for param in cls._autofilled_parameters) +  # autofilled params
            ", " +
            ", ".join(f"{param.name}={param.name}" for param in method.parameters)        # normal params
        )
        method.body = (
            f"return self.api.{reference.__name__}({arguments})",
        )

        return method
