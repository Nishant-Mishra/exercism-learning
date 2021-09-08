"""
Elyse is really looking forward to playing some poker (and other card games) during her upcoming trip to Vegas.
Being a big fan of "self-tracking" she wants to put together some small functions that will help her with
tracking tasks and has asked for your help thinking them through.
"""
from typing import List, NoReturn


def get_rounds(number: int) -> List[int]:
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return number in rounds


def card_average(hand: List[int]) -> float:
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    return card_average(hand) in {
        hand[len(hand) // 2],
        (hand[0] + hand[-1]) // 2
    }


def average_even_is_average_odd(hand: List[int]) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand: List[int]) -> NoReturn:
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
