""" Module representing the state of the orange die on the score card """
from typing import Optional

from model.colors.color_state import ColorState


class OrangeState(ColorState):
    """ Class Representing the Orange die state """

    def __init__(self):
        self.oranges = []

        # The score multipliers for each orange die
        self.multipliers = [1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3]

    def add_die(self, die_result: int) -> bool:
        if not self.is_next_die_valid(die_result):
            return False
        else:
            self.oranges.append(die_result * self.multipliers[len(self.oranges)])
            return True

    def is_next_die_valid(self, next: int) -> bool:
        next_index = len(self.oranges)
        # Valid IFF we have not already filled in every orange
        return next_index < len(self.multipliers)

    def get_utility(self, new_die: Optional[int] = None) -> int:
        if new_die and self.is_next_die_valid(new_die):
            return sum(self.oranges) + new_die * self.multipliers[len(self.oranges)]
        else:
            return sum(self.oranges)
