""" Module Representing the Score Card"""
from typing import Tuple, Optional, List, Dict

from model.colors.color_state import ColorState
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

    def get_utility(self, new_dice: Optional[List[Tuple[Color, int]]] = None) -> int:
        """
        Get the utility of the score card. If `new_dice` is specified (not None), it will return the utility of the card
        if those dice are added. Otherwise returns the utility of the card currently.
        :param new_dice: The optional new die color and result to include in the utility calculation
        :return: The utility of the card
        """
        color_map_copy: Dict[Color, ColorState] = {color: state.copy_state() for color, state in self._color_mapping.items()}

        if new_dice:
            for die in new_dice:
                color_map_copy[die[0]].add_die(die[1])

        return sum(map(lambda state: state.get_utility(), color_map_copy.values()))

    def __copy__(self):
        color_map_copy: Dict[Color, ColorState] = {color: state.copy_state() for color, state in
                                                   self._color_mapping.items()}
        new_card = ScoreCard()
        new_card._color_mapping = color_map_copy
        return new_card
