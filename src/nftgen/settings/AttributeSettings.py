from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, List, Dict, Any

from nftgen.model.Attribute import Attribute


@dataclass
class AttributeSettings:
    attribute: Attribute
    weight: float
    position: Tuple[float, float]
    anchor_point: Tuple[float, float]
    behind: bool
    slots:  List[Slot]


@dataclass
class Slot:
    feature: str
    position: Tuple[float, float]
    attributes_section: Dict[str, Any]
