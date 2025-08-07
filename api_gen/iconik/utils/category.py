from typing import Iterable
from functools import cache


@cache
def find_iconik_category(method_name: str) -> str | None:
    """
    Attempts to find a category name from a
    given method name following certain formats.

    Examples (input -> result):
    "v1_assets_asset_id_delete" -> "assets"
    "v1_assets_patch" -> None (this doesn't need an asset_id, so it shouldn't be in "assets")
    "v1_share_object_type_post" -> None
    "v1_sync_sessions_sync_session_id_delete" -> "sync_sessions"
    "v1_collections_collection_id_ancestors_get" -> "collections"

    Technical details:
    Category names can be longer than a single word,
    such as with "sync_sessions". This means we need
    to attempt getting the category name with varying
    "word spans".
    Furthermore, the results of this function are
    cached to allow the user to call this function
    even after all categories have been determined.
    """
    method_name = method_name.removeprefix("v1_")
    method_words = method_name.split('_')

    for word_span in range(len(method_words)):
        category = "_".join(method_words[:word_span])
        remaining_name = "_".join(method_words[word_span:])

        if remaining_name.startswith(f"{category[:-1]}_id"):
            return category

    return None


def determine_method_categories(method_names: Iterable[str]) -> set[str]:
    """
    Creates a set of categories found within the
    given method names.

    Example result:
    {
        "approvals", "assets", "collections",
        "custom_actions", "playlists", "projects",
        "sequences", "shares", "sync_sessions"
    }
    """
    categories = set()

    for method_name in method_names:
        category = find_iconik_category(method_name)
        if category is None:
            continue

        categories.add(category)

    return categories


def _get_shortened_method_name_with_category(method_name: str, category: str) -> str:
    special_method_names: dict[str, str] = {
        "patch": "edit",
        "put": "set",
    }

    method_name = method_name.removeprefix(f"v1_{category}_{category[:-1]}_id_")
    return special_method_names.get(method_name, method_name)  # replace method name by special name if needed

def _get_shortened_method_name_with_category_set(method_name: str, categories: set[str]) -> str:
    special_method_names: dict[str, str] = {
        "get": "get_{category}",
        "post": "create_{category}",
        "patch": "bulk_edit_{category}s",
        "put": "bulk_set_{category}s",
    }

    method_name = method_name.removeprefix("v1_")

    for category in categories:
        if method_name.startswith(category):
            short_name = method_name.removeprefix(f"{category}_")

            # only replace if the name after the category is exactly "get", "post", "patch", or "put"
            if short_name in special_method_names:
                return special_method_names[short_name].format(category=category[:-1])

    return method_name


def get_shortened_method_name(method_name: str, category: str | None, categories: set[str]) -> str:
    """
    Transforms the method name to be shorter and easier
    to understand. This will remove a part of the name
    related to the given category (if possible), so the
    returned name should only be used in the context of
    the given category.

    Examples(inputs -> result):
    "v1_assets_asset_id_delete", "assets" -> "delete"
    "v1_assets_post", None -> "create_asset" (using the 'categories' set)
    "v1_assets_get", None -> "get_asset"
    """
    if category is not None:
        return _get_shortened_method_name_with_category(method_name, category)
    else:
        return _get_shortened_method_name_with_category_set(method_name, categories)


if __name__ == '__main__':
    print(find_iconik_category("v1_assets_asset_id_delete"))
    print(find_iconik_category("v1_share_object_type_post"))
    print(find_iconik_category("v1_sync_sessions_sync_session_id_delete"))

    print("\n---------------\n")

    print(get_shortened_method_name("v1_assets_asset_id_delete", "assets", set()))
    print(get_shortened_method_name("v1_assets_post", None, {"assets",}))
    print(get_shortened_method_name("v1_assets_get", None, {"assets",}))
