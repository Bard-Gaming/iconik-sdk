from openapi_client.api.default_api import DefaultApi


CATEGORIES = {
    "approvals", "assets", "collections",
    "custom_actions", "playlists", "projects",
    "sequences", "shares", "sync_sessions"
}


class _ApiGeneratorMethod:
    special_methods: dict[str, str] = {
        "get": "get_list",
        "post": "create",
        "patch": "bulk_edit",
        "put": "bulk_set",
    }

    def __init__(self, name: str) -> None:
        self._original_name: str = name
        self._special_category: str | None = None
        self._category: str = self._determine_category()
        self._new_name: str = self._transform_original_name()

    @property
    def original_name(self) -> str:
        return self._original_name

    @property
    def new_name(self) -> str:
        return self._new_name

    @property
    def category(self) -> str:
        return self._category

    @property
    def is_special(self) -> bool:
        return self._special_category is not None

    @property
    def needs_special_return(self) -> bool:
        return self.is_special and (
                self.new_name.endswith("create") or
                self.new_name.startswith("get")
        )

    @property
    def special_return_class(self) -> str:
        if self._special_category is None:
            raise AttributeError(f"Attribute 'special_return_class' only exists on methods that need a special return.")

        return self._special_category.capitalize()

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

        if new_name in self.special_methods:
            self._special_category = self._category[:-1]
            new_name = f"{self._special_category}_{self.special_methods[new_name]}"
            self._category = "misc"

            return new_name

        new_name = new_name.removeprefix(f"{self.category[:-1]}_id_")

        new_name = new_name if new_name != "patch" else "edit"
        new_name = new_name if new_name != "put" else "set"

        if new_name == "get":
            self._special_category = self._category[:-1]
            new_name = f"get_{self._special_category}"
            self._category = "misc"

        return new_name

    def __repr__(self) -> str:
        return f"_ApiGeneratorMethod({self.original_name !r})"


class _ApiGeneratorClass:
    def __init__(self, name: str, parent_dir: str, methods: tuple[_ApiGeneratorMethod]) -> None:
        self.name = name
        self.parent_dir = parent_dir
        self.file_path = f"{self.parent_dir}/object/{self.name.lower()}.py"

    @property
    def import_stmt(self):
        import_path = self.file_path.replace('/', '.').removesuffix('.py')
        return f"from {import_path} import {self.name}"

    def generate(self) -> None:
        with open(self.file_path, "wt") as file:
            file.write("test")



class SimpleApiGenerator:
    def __init__(self, class_name: str = "GeneratedApiClass", api=None) -> None:
        self.class_name = class_name
        self.api = api if api is not None else DefaultApi()
        self._raw_method_names = self._get_raw_method_names()
        self._method_names = list(map(_ApiGeneratorMethod, self._raw_method_names))

    def _get_raw_method_names(self) -> list[str]:
        """
        Creates a list with all 'raw' method names that
        should be treated.
        """
        return [
            name for name in self.api.__dir__()
            if self._is_treated_method(name)
        ]

    def _is_treated_method(self, name: str) -> bool:
        """
        Filter out unwanted methods.

        Returns True if the method should be treated,
        and False if it shouldn't.
        """
        return (
            type(getattr(self.api, name)).__name__ == "method" and  # only treat methods
            name[0] != '_' and                                      # don't treat protected methods
            not name.endswith("with_http_info") and                 # unwanted method that clutters the API
            not name.endswith("without_preload_content")            # unwanted method that clutters the API
        )

    def _generate_class_header(self) -> str:
        """
        Returns the start of the Python class that is
        to be generated.
        """
        return (
            f"from {self.api.__module__} import {self.api.__class__.__name__}\n"
            f"\n"
            f"\n"
            f"class {self.class_name}:\n"
            f"    \"\"\"\n"
            f"     This class was generated using the SimpleApiGenerator.\n"
            f"    \"\"\"\n"
            f"\n"
            f"    def __init__(self, app_id: str, auth_token: str) -> None:\n"
            f"        self.api = {self.api.__class__.__name__}()\n"
            f"        self.app_id = app_id\n"
            f"        self.auth_token = auth_token\n"
            f"\n"
        )

    def _generate_method(self, method: _ApiGeneratorMethod) -> str:
        """
        Generates a method for the generated class.
        """

        parameters = ("self", "*args", "**kwargs")
        return_type = "any"
        method_call = f"self.api.{method.original_name}(*args, **kwargs, app_id=self.app_id, auth_token=self.auth_token)"

        return_stmt = (
            f"return {method_call}"

            if not method.needs_special_return else

            f"return {method.special_return_class}(\n"
            f"            {method_call}\n"
            f"        )"
        )

        if method.needs_special_return:
            return_type = method.special_return_class

        return (
            f"    def {method.new_name}(\n"
            f"{',\n'.join(f'        {param}' for param in parameters)}"
            f"\n"
            f"    ) -> {return_type}:\n"
            f"        {return_stmt}\n"
            f"\n"
        )

    def _generate_footer(self) -> str:
        """
        Returns the end of the Python class that is
        to be generated.
        """
        return (
            f"    def __repr__(self) -> str:\n"
             "        return f'{self.__class__.__name__}({self.app_id !r})'\n"
            f"\n"
        )

    def generate(self, file_path: str) -> None:
        with open(file_path, "wt") as file:
            file.write(self._generate_class_header())
            for method in self._method_names:
                # if method.category == "misc":
                file.write(self._generate_method(method))

    def __repr__(self) -> str:
        return f"SimpleApiGenerator({self.class_name !r}, {self.api.__class__.__name__}())"


a = SimpleApiGenerator("IconikAPI")
a.generate("generated.py")
