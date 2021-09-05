"""
The goal of this exercise is to create a way:

to look up the numerical value associated with a particular color band
to list the different band colors
Mnemonics map the colors to the numbers, that, when stored as an array, happen to map to their index in the array:

    Better Be Right Or Your Great Big Values Go Wrong.

"""
from typing import List

_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]


def color_code(color: str) -> int:
    """

    :param color: str: The color of the resistor whose 'code' is desired
    :return: int: The digit code for the input color
    """
    return _COLORS.index(color)


def colors() -> List[str]:
    """

    :return: The list of colors in order of their value
    """
    return _COLORS
