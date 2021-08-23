import random


class Robot:
    alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

    def __init__(self):
        self._name = self._generate_rand_name()

    @classmethod
    def _generate_rand_name(cls):
        random.seed()
        _name = ''.join(random.choices(cls.alphabet, k=2))
        _name += f'{random.choice(range(1000)):03d}'
        return _name

    @property
    def name(self):
        if not self._name:
            self._name = self._generate_rand_name()
        return self._name

    def reset(self):
        self._name = ""
