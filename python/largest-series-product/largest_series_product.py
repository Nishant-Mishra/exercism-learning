"""
    Given a string of digits, calculate the largest product for a contiguous substring of digits of length n.

        For example, for the input '1027839564', the largest product for a series of 3 digits is 270 (9 * 5 * 6),
        and the largest product for a series of 5 digits is 7560 (7 * 8 * 3 * 9 * 5).

    Note that these series are only required to occupy adjacent positions in the input;
    the digits need not be numerically consecutive.

        For the input '73167176531330624919225119674426574742355349194934',
        the largest product for a series of 6 digits is 23520.

    Implementation note: In case of invalid inputs to the 'largest_product' function your program should raise a
    ValueError with a meaningful error message.

    Feel free to reuse your code from the 'series' exercise!
"""
import functools
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


def largest_product(series: str, size: int) -> int:
    """

    :param series: str: A string of digits
    :param size: int: Size of the substring for which the max product is to be determined
    :return: int: Max product
    """
    if size == 0:
        return 1

    max_prod = 0
    for num_str in slices(series, size):
        prod = functools.reduce(lambda acc, elem: int(elem) * int(acc), num_str)
        if prod > max_prod:
            max_prod = prod

    return max_prod
