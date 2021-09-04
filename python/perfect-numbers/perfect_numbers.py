"""
Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme
for positive integers.

The Greek mathematician Nicomachus devised a classification scheme for positive integers,
identifying each as belonging uniquely to the categories of perfect, abundant, or deficient based on their aliquot sum.
The aliquot sum is defined as:
    the sum of the factors of a number not including the number itself.
    For example, the aliquot sum of 15 is (1 + 3 + 5) = 9

Perfect: aliquot sum = number
    6 is a perfect number because (1 + 2 + 3) = 6
    28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
Abundant: aliquot sum > number
    12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
    24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
Deficient: aliquot sum < number
    8 is a deficient number because (1 + 2 + 4) = 7
    Prime numbers are deficient
Implement a way to determine whether a given number is perfect.
Depending on your language track, you may also need to implement a way to determine whether a given number is
abundant or deficient.
"""
from math import sqrt, ceil
from typing import List


def _factors(number: int) -> List[int]:
    """

    :param number: int: Number to find factors for
    :return: List[int]: List of factors of 'number'

    Find all factors of the number except the number itself
    """
    factors = []
    limit = ceil(sqrt(number))
    for fac in range(1, limit):
        if number % fac == 0:
            factors.extend({fac, number // fac})
    return factors


def _aliquot_sum(number: int) -> int:
    """

    :param number: int: The number for which the aliquot sum is to be determined
    :return: int: The aliquot sum

    Find the aliquot sum as described in the module docstring
    """
    return sum(_factors(number)) - number


def classify(number: int) -> str:
    """

    :param number: The number to be classified
    :return: str: The class of number: 'perfect', 'deficient' or 'abundant'

    Classify the number based on its aliquot sum.
    """
    if number <= 0:
        raise ValueError("Only Positive Integers ( > 0) allowed")

    aliquot_sum = _aliquot_sum(number)
    if aliquot_sum == number:
        return 'perfect'
    if aliquot_sum < number:
        return 'deficient'
    return 'abundant'
