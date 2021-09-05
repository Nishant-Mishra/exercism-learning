"""
Given an age in seconds, calculate how old someone would be on:

    Mercury: orbital period 0.2408467 Earth years
    Venus: orbital period 0.61519726 Earth years
    Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
    Mars: orbital period 1.8808158 Earth years
    Jupiter: orbital period 11.862615 Earth years
    Saturn: orbital period 29.447498 Earth years
    Uranus: orbital period 84.016846 Earth years
    Neptune: orbital period 164.79132 Earth years

So if you were told someone were 1,000,000,000 seconds old, you should be able to say that
they're 31.69 Earth-years old.

"""
EARTH_SEC_TO_EARTH_YEAR = 31557600
EARTH_YEAR_TO_PLANET_YEAR = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1.0,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132
}


class SpaceAge:
    """
    Return the age of person (given in seconds) on all 8 planets
    """
    def __init__(self, seconds: int):
        self._earth_years = seconds / EARTH_SEC_TO_EARTH_YEAR

    def _on_planet(self, planet: str) -> float:
        """

        :param planet: str: String name of the planet
        :return: float: Age in planet-years on the given planet, rounded to 2 decimal places
        """
        planet_age = self._earth_years / EARTH_YEAR_TO_PLANET_YEAR[planet]
        return round(planet_age, 2)

    def on_mercury(self) -> float:
        """
        :return: float: Age in mercury, rounded to 2 decimal places
        """
        return self._on_planet('mercury')

    def on_venus(self) -> float:
        """
        :return: float: Age in venus, rounded to 2 decimal places
        """
        return self._on_planet('venus')

    def on_earth(self) -> float:
        """
        :return: float: Age in earth, rounded to 2 decimal places
        """
        return self._on_planet('earth')

    def on_mars(self) -> float:
        """
        :return: float: Age in mars, rounded to 2 decimal places
        """
        return self._on_planet('mars')

    def on_jupiter(self) -> float:
        """
        :return: float: Age in jupiter, rounded to 2 decimal places
        """
        return self._on_planet('jupiter')

    def on_saturn(self) -> float:
        """
        :return: float: Age in saturn, rounded to 2 decimal places
        """
        return self._on_planet('saturn')

    def on_uranus(self) -> float:
        """
        :return: float: Age in uranus, rounded to 2 decimal places
        """
        return self._on_planet('uranus')

    def on_neptune(self) -> float:
        """
        :return: float: Age in neptune, rounded to 2 decimal places
        """
        return self._on_planet('neptune')
