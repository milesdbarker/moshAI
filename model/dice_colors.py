""" Module enumerating the dice colors """
from enum import Enum
from typing import List


class Color(Enum):
    GREEN = "green"
    ORANGE = "orange"
    PURPLE = "purple"


def get_all_colors() -> List[Color]:
    """
    Get a list of all the colors.
    :return: The list of colors
    """
    return [Color.GREEN, Color.ORANGE, Color.PURPLE]
