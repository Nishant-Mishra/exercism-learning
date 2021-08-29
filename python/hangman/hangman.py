# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"
UNKNOWN = '_'


class Hangman:
    def __init__(self, word: str):
        self._remaining_guesses = 10
        self.status = STATUS_ONGOING
        self._answer = word
        self._guess = ['_'] * len(self._answer)
        self._done = set()

    @property
    def remaining_guesses(self):
        return self._remaining_guesses - 1

    def _has_letter(self, char):
        positions = []
        pos = -1
        while True:
            try:
                pos = self._answer.index(char, pos + 1)
            except ValueError:
                break
            else:
                positions.append(pos)
                self._done.add(char)

        return positions

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("No guesses remaining !!")

        if char in self._done or char not in self._answer:
            self._remaining_guesses -= 1

        positions = self._has_letter(char)

        for pos in positions:
            self._guess[pos] = char

        self.update_status()

    def get_masked_word(self):
        return ''.join(self._guess)

    def update_status(self):
        if self._remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif set(self._answer) == self._done:
            self.status = STATUS_WIN

    def get_status(self):
        return self.status
