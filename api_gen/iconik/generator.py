import logging

from api_gen.file_generator import FileGenerator, FileGeneratorImport
from api_gen.class_generator import ClassGenerator, ClassGeneratorAttribute
from api_gen.iconik.method_generator import IconikMethodGenerator


__all__ = ["IconikApiGenerator"]

from api_gen.iconik.utils import transform_case

from api_gen.iconik.utils.category import find_iconik_category, determine_method_categories, get_shortened_method_name

LOGGER = logging.getLogger("iconik_api_generator")


class IconikApiGenerator:
    def __init__(self, api_name: str, api_provider: any) -> None:
        self.api_name = api_name
        self.api_provider = api_provider

        self._imports = (
            FileGeneratorImport(self.api_provider.__module__, (self.api_provider.__class__.__name__,)),
            FileGeneratorImport("pydantic.fields", ("*",)),
            FileGeneratorImport("pydantic", ("*",)),
            FileGeneratorImport("typing"),
        )

    def generate(self, dir_path: str) -> None:
        LOGGER.info(f"Generating {self.api_name} in {dir_path !r}")
        files = self._generate_files()

        for file in files:
            file.generate(dir_path)

    def _is_treated_method(self, name: str) -> bool:
        """
        Filter out unwanted methods.

        Returns True if the method should be treated,
        and False if it shouldn't.
        """
        return (
            type(getattr(self.api_provider, name)).__name__ == "method" and  # only treat methods
            name[0] != '_' and                                               # don't treat protected methods
            not name.endswith("with_http_info") and                          # unwanted method that clutters the API
            not name.endswith("without_preload_content")                     # unwanted method that clutters the API
        )

    def _get_method_names(self) -> tuple[str, ...]:
        """
        Creates a list with all 'raw' method names that
        should be treated.
        """
        return tuple(
            name for name in self.api_provider.__dir__()
            if self._is_treated_method(name)
        )

    def _get_method_table(self) -> dict[str, list[IconikMethodGenerator]]:
        method_names = self._get_method_names()
        categories = determine_method_categories(method_names)
        table = {
            category: []
            for category in categories
        }

        table["misc"] = []  # add 'misc' category for methods without distinct category

        for method_name in method_names:
            category = find_iconik_category(method_name)
            shortened_name = get_shortened_method_name(method_name, category, categories)

            method = IconikMethodGenerator.from_reference(
                shortened_name,
                getattr(self.api_provider, method_name)
            )

            table[category if category is not None else "misc"].append(method)

        return table

    def _generate_files(self) -> tuple[FileGenerator, ...]:
        _method_table = self._get_method_table()
        api_methods = _method_table.pop("misc")

        file_classes = tuple(
            ClassGenerator(
                transform_case(name[:-1], "CAMEL_CASE"),
                (
                    ClassGeneratorAttribute("app_id", str),
                    ClassGeneratorAttribute("auth_token", str),
                    ClassGeneratorAttribute(f"{name[:-1]}_id", str),
                ),
                methods
            )
            for name, methods in _method_table.items()
        )

        return tuple(
            FileGenerator(
                transform_case(file_class.name, "SNAKE_CASE"),
                self._imports,
                file_class
            )
            for file_class in file_classes
        )

    def __repr__(self) -> str:
        return f"IconikApiGenerator({self.api_name !r}, {self.api_provider !r})"


if __name__ == '__main__':
    from openapi_client.api.default_api import DefaultApi
    a = IconikApiGenerator("IconikApi", DefaultApi())
    a.generate("test_dir")
