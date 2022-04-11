""" Module Representing the Game State"""
import random
from typing import Dict

from model.dice_colors import Color, get_all_colors
from model.scorecard import ScoreCard


class GameState:
    """ Class representing the Game State of Ganz Schon Clever"""

    def __init__(self):
        """ Initialize a new GameState """

        self._turn_number = 1
        self.roll_number = 1
        self._roll = None
        self.card = ScoreCard()
        self._available_dice = get_all_colors()

    def roll_dice(self) -> Dict[Color, int]:
        """
        Roll the dice
        :return: A dictionary mapping from each dice color to the result of the die
        """
        roll = dict()
        for color in self._available_dice:
            roll.update({color: random.randint(1, 6)})
        self._roll = roll
        return roll

    def choose_die(self, die: Color) -> bool:
        """
        Choose the dice to take for the roll. If the choice is valid, this returns true and applies the choice (resetting the roll).
        Otherwise, it returns false and the previous roll is not reset (another choice must be made).
        PREREQUISITE: Dice must have been rolled first (Roll dice after each successful call of this method).
        :param die: The dice color to take
        :return: Whether or not the choice was valid (successful)
        """
        assert self._roll is not None

        if die not in self._roll or not self.card.add_die(die, self._roll[die]):
            return False

        self._roll = None
        if self.roll_number < 3:
            self.roll_number += 1
            self._available_dice.remove(die)
        else:
            self.roll_number = 1
            self._turn_number += 1
            self._available_dice = get_all_colors()
        return True

    def skip_choice(self):
        """
        Skip the choice for this roll and move onto the next roll for the turn (or the next turn if the turn is now over).
        Dice don't have to be rolled to call this method, although the intention is to only call when a roll results in
        no possible moves.
        """
        self._roll = None
        if self.roll_number < 3:
            self.roll_number += 1
        else:
            self.roll_number = 1
            self._turn_number += 1
            self._available_dice = get_all_colors()

    def is_game_over(self) -> bool:
        """
        Is the game over? The game is over if all turns have been played.
        :return: Whether or not the game is over
        """
        # If the turn number exceeds 6, then 6 turns have been played and the game is over
        return self._turn_number > 6

    def get_utility(self) -> int:
        """
        Get the utility of the game state.
        :return: The total utility
        """
        return self.card.get_utility()
