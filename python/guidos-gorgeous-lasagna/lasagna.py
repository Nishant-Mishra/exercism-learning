"""
Create utility functions to help cook lasgna
"""


EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining if remaining > 0 else 0


def preparation_time_in_minutes(layers: int) -> int:
    """
    :param layers: int  the number of layers you want to add to the lasagna
    :return: int  minutes you would spend making the layers

    Function that takes the number of layers you want to add to the lasagna
    as an argument and returns how many minutes you would spend making them.
    Assume each layer takes 2 minutes to prepare.
    """
    return layers * 2


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int):
    """
    :param layers: int  the number of layers you want to add to the lasagna
    :param elapsed_bake_time: int baking time already elapsed
    :return: int  total number of minutes you've been cooking,

    Function should return the total number of minutes you've been cooking,
    or the sum of your preparation time and the time the lasagna has already
    spent baking in the oven.
    """
    return elapsed_bake_time + preparation_time_in_minutes(layers)
    