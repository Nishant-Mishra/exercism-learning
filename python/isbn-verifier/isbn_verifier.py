"""
Given a string the program should check if the provided string is a valid ISBN-10.
Putting this into place requires some thinking about preprocessing/parsing of the string prior to
calculating the check digit for the ISBN.

The program should be able to verify ISBN-10 both with and without separating dashes.
"""
from typing import List

MOD_ISBN10 = 11


def is_valid(isbn: str) -> bool:
    """

    :param isbn: str - An ISBN string to be validated
    :return: bool - Whether given ISBN string is valid or not
    """
    return is_valid_recursive(list(isbn), 0, 10)


def is_valid_recursive(isbn_ch_list: List[str], chksum: int, multiplier: int) -> bool:
    """

    :param isbn_ch_list: List of characters in the ISBN String
    :param chksum: Checksum calculated for the already visited digits
    :param multiplier: Currrent Multiplier
    :return: bool: Whether the given ISBN is valid or not
    """
    # ISBN digits exhausted...
    if not isbn_ch_list:
        # And we checked 10 digits...
        if multiplier == 0:
            return chksum % MOD_ISBN10 == 0
        # Less digits were supplied
        return False

    first, *rest = isbn_ch_list

    # Skip over '-'
    if first == '-':
        return is_valid_recursive(rest, chksum, multiplier)

    # If we reached chksum digit with value '10'
    if first == 'X':
        # If this is the last digit
        if not rest:
            return is_valid_recursive(rest, chksum + 10, multiplier - 1)
        # We found 'X' in middle
        return False

    # Calculate chksum and proceed...
    if first.isdigit():
        return is_valid_recursive(rest, chksum + multiplier * int(first), multiplier - 1)
    # Found an alien character... Not Allowed !!
    return False


if __name__ == '__main__':
    print(is_valid(""))
