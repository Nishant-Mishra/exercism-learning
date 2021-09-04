"""
Given a string the program should check if the provided string is a valid ISBN-10.
Putting this into place requires some thinking about preprocessing/parsing of the string prior to
calculating the check digit for the ISBN.

The program should be able to verify ISBN-10 both with and without separating dashes.
"""

MOD_ISBN10 = 11


def is_valid(isbn: str) -> bool:
    """

    :param isbn: str - An ISBN string to be validated
    :return: bool - Whether given ISBN string is valid or not
    """
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False

    try:
        _sum = sum(int(dig) * (10 - i) for i, dig in enumerate(isbn[:-1]))
    except ValueError:
        return False

    check_dig = isbn[-1].replace('X', '10')
    try:
        check_dig = int(check_dig)
    except ValueError:
        return False

    return not bool((_sum + check_dig) % MOD_ISBN10)
