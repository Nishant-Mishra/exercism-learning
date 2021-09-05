"""
In this exercise you are going to create a helpful program
so that you don't have to remember the values of the bands.

The program will take color names as input and output a two digit number,
even if the input is more than two colors!
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


def value(colors: List[str]) -> int:
    """

    :param colors: List[str]: List of resistor color names
    :return: int: An integer formed using the value of resistor color at 1st and 2nd positions (only)
    """
    return _COLORS.index(colors[0]) * 10 + _COLORS.index(colors[1])
