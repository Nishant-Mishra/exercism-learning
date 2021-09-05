"""
Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

Write code that shows:

how many grains were on a given square, and
the total number of grains on the chessboard

"""


def square(number: int) -> int:
    """

    :param number: int: The square number at which number of grains are to be determined
    :return: int: The number of grains in the given square
    :raises: ValueError: If number is not in range [1, 64]
    """
    if 0 < number <= 64:
        return 2 ** (number - 1)
    raise ValueError("Invalid square number !!")


def total() -> int:
    """

    :return: int: Return sum of number of grains in each of the 64 squares, i.e. 2^64 - 1
    """
    # The sum of the geometric series 1 + 2 + 4 + 8... 64 terms is 2^64 - 1
    return 2**64 - 1
