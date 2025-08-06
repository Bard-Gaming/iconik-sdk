from api_gen.iconik_generator import IconikMethodGenerator
from typing import Collection


def v1_assets_asset_id_patch(auth_token: str, app_id: str, a: str | None, b) -> None:
    print("hi")

method = IconikMethodGenerator(v1_assets_asset_id_patch)
print(f"Method of class {method.class_name}:")
print(method.generate(0))
