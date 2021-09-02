"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


from collections import Counter
from typing import List, Callable


_NUM_CATEGORIES = 12

# Score categories.
(YACHT, ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE,
 FOUR_OF_A_KIND, LITTLE_STRAIGHT, BIG_STRAIGHT, CHOICE) = range(_NUM_CATEGORIES)


def _yacht_score(dice: List[int]) -> int:
    return 50 if len(set(dice)) == 1 else 0


def _nums_score_gen(win_num: int) -> Callable:
    def num_score(dice: List[int]) -> int:
        return dice.count(win_num) * win_num
    return num_score


def _full_house_score(dice: List[int]) -> int:
    counts = Counter(dice)
    if set(counts.values()) == {2, 3}:
        return sum(dice)
    return 0


def _four_of_a_kind_score(dice: List[int]) -> int:
    counts = Counter(dice)
    mc = counts.most_common(1)[0]
    return mc[0] * 4 if mc[1] >= 4 else 0


def _little_straight_score(dice: List[int]) -> int:
    return 30 if set(dice) == {1, 2, 3, 4, 5} else 0


def _big_straight_score(dice: List[int]) -> int:
    return 30 if set(dice) == {2, 3, 4, 5, 6} else 0


def _choice_score(dice: List[int]) -> int:
    return sum(dice)


category_score_map = {
    YACHT:           _yacht_score,
    ONES:            _nums_score_gen(1),
    TWOS:            _nums_score_gen(2),
    THREES:          _nums_score_gen(3),
    FOURS:           _nums_score_gen(4),
    FIVES:           _nums_score_gen(5),
    SIXES:           _nums_score_gen(6),
    FULL_HOUSE:      _full_house_score,
    FOUR_OF_A_KIND:  _four_of_a_kind_score,
    LITTLE_STRAIGHT: _little_straight_score,
    BIG_STRAIGHT:    _big_straight_score,
    CHOICE:          _choice_score
}


def score(dice, category):
    return category_score_map[category](dice)

