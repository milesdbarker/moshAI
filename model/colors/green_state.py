""" Module representing the state of the green die on the score card """
from typing import Optional

from model.colors.color_state import ColorState


class GreenState(ColorState):
    """ Class Representing the Green die state """

    def __init__(self):
        self.greens = []

        # The thresholds required for choosing the green die (roll value must be >= the threshold at every index)
        self.thresholds = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]

        # The scores for green. 0 is added at the beginning if there are no greens
        self.scores = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]

    def add_die(self, die_result: int) -> bool:
        if not self.is_next_die_valid(die_result):
            return False
        else:
            self.greens.append(die_result)
            return True

    def is_next_die_valid(self, next: int) -> bool:
        next_index = len(self.greens)
        # Valid IFF we have not already filled in every green and if the die result is at least the next threshold
        return next_index < len(self.thresholds) and next >= self.thresholds[next_index]

    def get_utility(self, new_die: Optional[int] = None) -> int:
        if new_die and self.is_next_die_valid(new_die):
            return self.scores[len(self.greens) + 1]
        else:
            return self.scores[len(self.greens)]

    def get_score(self) -> int:
        return self.scores[len(self.greens)]
