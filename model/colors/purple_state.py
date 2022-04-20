""" Module representing the state of the purple die on the score card """
from typing import Optional

from model.colors.color_state import ColorState


class PurpleState(ColorState):
    """ Class Representing the Purple die state """

    def __init__(self):
        self.purples = []

        self.max_purples = 11

    def add_die(self, die_result: int) -> bool:
        if not self.is_next_die_valid(die_result):
            return False
        else:
            self.purples.append(die_result)
            return True

    def is_next_die_valid(self, next: int) -> bool:
        next_index = len(self.purples)
        last_purple = 0 if next_index == 0 else self.purples[-1]
        # Valid IFF we have not already filled in every purple and the next die is greater than the last purple (or the last purple is a 6)
        return next_index < self.max_purples and (last_purple == 6 or next > last_purple)

    def get_utility(self, new_die: Optional[int] = None) -> int:
        if new_die and self.is_next_die_valid(new_die):
            return sum(self.purples) + new_die
        else:
            return sum(self.purples)

    def get_score(self) -> int:
        return sum(self.purples)
