""" Module representing the state of the blue die on the score card """
from typing import Optional

from model.colors.color_state import ColorState


class BlueState(ColorState):
    """ Class Representing the Blue die state """

    def __init__(self):
        self.blues = []

        # The scores for blue. 0 is added at the beginning if there are no blues
        self.scores = [0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56]

    def add_die(self, die_result: int) -> bool:
        if not self.is_next_die_valid(die_result):
            return False
        else:
            self.blues.append(die_result)
            return True

    def is_next_die_valid(self, next: int) -> bool:
        # Valid IFF we have not already filled in that blue
        return next not in self.blues

    def get_utility(self, new_die: Optional[int] = None) -> int:
        if new_die and self.is_next_die_valid(new_die):
            return self.scores[len(self.blues) + 1]
        else:
            return self.scores[len(self.blues)]
