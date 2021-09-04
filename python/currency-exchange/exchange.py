"""
Your friend Chandler plans to visit exotic countries all around the world.
Sadly, Chandler's math skills aren't good. He's pretty worried about being scammed
with currency exchange during his trip - and he wants you to make a currency calculator for him.
"""


def estimate_value(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - the estimated value of the foreign currency you can receive
    based on your budget and the current exchange rate.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - the amount left of your starting currency after exchanging exchanging_value.
    """
    return budget - exchanging_value


def get_value(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int amount of bills you received.
    :return: int - the total value of bills you now have.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - the number of bills after exchanging all your money.
    """
    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - the maximum value you can get considering the budget, exchange_rate, spread, & denomination.
    """
    exch_rate = exchange_rate * (1 + spread / 100)
    est_val = estimate_value(budget, exch_rate)
    bills = get_number_of_bills(est_val, denomination)

    return get_value(denomination, bills)


def unexchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int -  the unexchangeable value considering the budget, exchange_rate, spread, & denomination.
    """
    exch_val = exchangeable_value(budget, exchange_rate, spread, denomination)
    exch_rate = exchange_rate * (1 + spread / 100)
    est_val = estimate_value(budget, exch_rate)

    return int(est_val - exch_val)
