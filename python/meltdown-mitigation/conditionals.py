"""
In this exercise, we'll develop a simple control system for a nuclear reactor.

For a reactor to produce the power it must be in a state of criticality.
If the reactor is in a state less than criticality, it can become damaged.
If the reactor state goes beyond criticality, it can overload and result in a meltdown.
We want to mitigate the chances of meltdown and correctly manage reactor state.

The following three tasks are all related to writing code for maintaining ideal reactor state.
"""


efficiency_map = {
    range(80, 101): 'green',
    range(60, 80): 'orange',
    range(30, 60): 'red',
    range(0, 30): 'black'
}


def is_criticality_balanced(temperature: int, neutrons_emitted: int) -> bool:
    """
    :param temperature: int - Temperatur of the reactor core
    :param neutrons_emitted: int - Neutrons emitted per second
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return all((temperature < 800,
                neutrons_emitted > 500,
                temperature * neutrons_emitted < 500_000))


def reactor_efficiency(voltage: int, current: int, theoretical_max_power: int) -> str:
    """
    :param voltage: int - Voltage of the generated Power
    :param current: int - Current of the generated Power
    :param theoretical_max_power: int - Max power that can be generated theoretically
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as `(generated power/ theoretical max power) * 100`
    where generated `power = voltage * current`
    """
    eff = (100 * voltage * current) / theoretical_max_power
    for key, val in efficiency_map.items():
        if key.start <= eff < key.stop:
            return val
    return ''


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """
    :param temperature: int - Temperatur of the reactor core
    :param neutrons_produced_per_second: int - Neutrons produced per second
    :param threshold: int - Threshold used to decide the criticality of the reactor
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    Create a fail-safe mechanism to avoid overload and meltdown.
    This mechanism will determine if the reactor is below, at, or above the ideal criticality threshold.
    Criticality can then be increased, decreased, or stopped by inserting (or removing) control rods into the reactor.

    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    """
    criticality = temperature * neutrons_produced_per_second
    if criticality < 0.4 * threshold:
        return 'LOW'
    if abs(criticality - threshold) <= 0.1 * threshold:
        return 'NORMAL'
    return 'DANGER'
