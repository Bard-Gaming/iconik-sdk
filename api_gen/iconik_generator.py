from typing import Collection, Callable

from api_gen.method_generator import ReferencedMethodGenerator, MethodGeneratorParameter


__all__ = ["IconikMethodGenerator"]


CATEGORIES = {
    "approvals", "assets", "collections",
    "custom_actions", "playlists", "projects",
    "sequences", "shares", "sync_sessions"
}


class IconikMethodGenerator(ReferencedMethodGenerator):
    _special_methods: dict[str, str] = {
        "get": "get_list",
        "post": "create",
        "patch": "bulk_edit",
        "put": "bulk_set",
    }

    def __init__(self, reference: Callable) -> None:
        super().__init__("TemporaryName", reference)
        self._category = self._determine_category()
        self._return_wrapper: str | None = None
        self.name = self._transform_original_name()

    @property
    def category(self) -> str:
        return self._category

    @property
    def class_name(self) -> str:
        return self._category[:-1].capitalize()

    def _determine_category(self) -> str:
        """
        Returns the category of the given method's name.
        This will always return a category, even if the
        method isn't in a distinct category (if there is
        no category, the returned value will just be 'misc')
        """
        for category in CATEGORIES:
            if category in self.original_name:
                return category

        return "misc"

    def _transform_original_name(self) -> str:
        """
        Transforms the original name into an easier
        to find, more digestible method name.
        """
        new_name = self.original_name.removeprefix("v1_")
        new_name = new_name.removeprefix(f"{self.category}_")

        if new_name in self._special_methods:
            method_category = self._category[:-1]
            new_name = f"{method_category}_{self._special_methods[new_name]}"
            self._return_wrapper = method_category.capitalize()
            self._category = "misc"

            return new_name

        new_name = new_name.removeprefix(f"{self.category[:-1]}_id_")

        new_name = new_name if new_name != "patch" else "edit"
        new_name = new_name if new_name != "put" else "set"

        if new_name == "get":
            method_category = self._category[:-1]
            new_name = f"get_{method_category}"
            self._return_wrapper = method_category.capitalize()
            self._category = "misc"

        return new_name

    def _transform_parameters(
            self,
            parameters: Collection[MethodGeneratorParameter]
    ) -> Collection[MethodGeneratorParameter]:
        return tuple(
            filter(
                # Remove app_id and auth_token from parameters
                lambda param: param.name != "app_id" and param.name != "auth_token",
                parameters
            )
        )

    def _build_body_from_reference(self, parameters: Collection[MethodGeneratorParameter]) -> Collection[str]:
        arguments = ", ".join(f"{param.name}={param.name}" for param in parameters)

        # Add App ID and Auth Token that were removed earlier:
        return (
            f"return self.api.{self.original_name}(app_id=self.app_id, auth_token=self.auth_token, {arguments})",
        )
