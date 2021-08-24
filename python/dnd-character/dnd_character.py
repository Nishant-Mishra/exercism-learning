import random
from math import floor


class Character:
    def __init__(self):
        random.seed()
        self.strength = self._get_random_ability_value()
        self.dexterity = self._get_random_ability_value()
        self.constitution = self._get_random_ability_value()
        self.intelligence = self._get_random_ability_value()
        self.wisdom = self._get_random_ability_value()
        self.charisma = self._get_random_ability_value()
        self._abilities = [self.constitution, self.intelligence, self.strength, self.dexterity,
                           self.charisma, self.wisdom]
        self.hitpoints = modifier(self.constitution) + 10

    @staticmethod
    def _get_random_ability_value():
        rand_vals = []
        for i in range(4):
            rand_vals.append(random.choice(range(1, 7)))
        rand_vals.remove(min(rand_vals))
        return sum(rand_vals)

    def ability(self):
        return self._abilities[random.choice(range(6))]


def modifier(constitution):
    return floor((constitution - 10) / 2)
