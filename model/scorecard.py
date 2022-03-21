""" Module Representing the Score Card"""
from typing import Tuple, Optional

from model.colors.green_state import GreenState
from model.colors.orange_state import OrangeState
from model.colors.purple_state import PurpleState
from model.dice_colors import Color


class ScoreCard:
    """ Class representing the score card of Ganz Schon Clever"""

    def __init__(self):
        """ Initialize a new ScoreCard """
        self._green_state = GreenState()
        self._orange_state = OrangeState()
        self._purple_state = PurpleState()
        self._color_mapping = {
            Color.GREEN: self._green_state,
            Color.ORANGE: self._orange_state,
            Color.PURPLE: self._purple_state
        }

    def add_die(self, die: Color, result: int) -> bool:
        """
        Try to add the die result to the score card (returns false if the die cannot be added).
        :param die: The color of the die chosen
        :param result: The result of the roll for that color
        :return: Whether or not the die could be added to the score card
        """
        state = self._color_mapping[die]
        if state.is_next_die_valid(result):
            state.add_die(result)
            return True
        else:
            return False

    def get_utility(self, new_die: Optional[Tuple[Color, int]] = None) -> int:
        """
        Get the utility of the score card. If `new_die` is specified (not None), it will return the utility of the card
        if that die is added. Otherwise returns the utility of the card currently.
        :param new_die: The optional new die color and result to include in the utility calculation
        :return: The utility of the card
        """
        if new_die:
            self._color_mapping[new_die[0]].add_die(new_die[1])

        return self._green_state.get_utility() + self._orange_state.get_utility() + self._purple_state.get_utility()
