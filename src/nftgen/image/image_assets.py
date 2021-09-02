import os
import warnings
from typing import Optional

from PIL import Image

from nftgen.model.Attribute import Attribute
from nftgen.model.Position import Position
from nftgen.settings import config


def create_background() -> Image:
    return Image.new(mode="RGBA", size=(config.size, config.size), color=config.background_color)


def _get_asset(asset_name: str, scale: Optional[float] = None) -> Image:
    path = f"{config.assets_dir}/{asset_name}.png"
    if not os.path.exists(path):
        warnings.warn(f"Could not find asset: {path}")
        return None
    image = Image.open(path)
    if scale is not None and scale != 1:
        image = image.resize((round(image.width * scale), round(image.height * scale)))
    return image


def get_shadow() -> Image:
    return _get_asset("shadow", config.assets_scale)


def get_image(attribute: Attribute) -> Image:
    return _get_asset(f"{attribute.feature}/{attribute.name}", config.assets_scale)


def compose(background: Image, image: Image, position: Position):
    background.alpha_composite(image, position.point)

