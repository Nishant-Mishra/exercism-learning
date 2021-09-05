"""
Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.

For example, the string "49142" has the following 3-digit series:

    "491"
    "914"
    "142"

"""
from typing import List


def slices(series: str, length: int) -> List[str]:
    """

    :param series: str: A sequence of integers
    :param length: int: Length of sub-sequences to be returned
    :return: List[str]: A list of all sub-series of length 'length' of the given series
    """
    # Check if given length is non-zero and less than (or equal) the length of string
    if 0 < length <= len(series) and series:
        return [series[start:(start + length)] for start in range(0, len(series) - length + 1)]
    raise ValueError("Invalid inputs for slicing the series !!")
