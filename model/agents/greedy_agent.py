from typing import Dict, Tuple, List
import random

from model.agents.abstract_agent import Agent
from model.gamestate import GameState
from model.dice_colors import Color, get_all_colors


class GreedyAgent(Agent):

    def choose_die(self, dice: Dict[Color, int]) -> Color:
        roll = self.game_state.roll_number
        sorted_dice: List[Tuple[Color, int]] = [(c, v) for c, v in sorted(dice.items(), key=lambda d: d[1])]
        sorted_dice.reverse()


        # Want to make sure that no matter what, we will be able to roll at least one die for each roll in the turn'
        # By default, that means the highest {3 - roll #} dice get left out. But because of the ways that ties work,
        # Add back in the highest dice if there is a tie (i.e. a roll of 5, 5, 5, 3, 2 we can look at every die and
        # still have at least two left for the last two rolls of the turn)
        index = 3 - roll
        offset = 0
        for i in range(index, 0, -1):
            if len(sorted_dice) < i and sorted_dice[i][1] == sorted_dice[index][1]:
                offset += 1
            else:
                continue
        dice_priority = self.prioritize_dice(sorted_dice[index - offset:])

        for die in dice_priority:
            if self.choose_die_wrapper(die[0], die[1]):
                self.colors_chosen[die[0]] += 1
                return die[0]
        self.game_state.skip_choice()
        return None

    def prioritize_dice(self, dice: List[Tuple[Color, int]]) -> List[Tuple[Color, int]]:
        """
        Prioritize the dice based on the added utility each one provides.
        :param dice: The dice to prioritize
        :return: The dice in prioritized order (preferred die is first in the returned list)
        """
        utilities: Dict[Color, int] = {}
        for die in dice:
            if die[0] != Color.WHITE:
                added_utility = self.game_state.card.get_utility([(die[0], die[1])]) - self.game_state.card.get_utility()
                utilities[die[0]] = added_utility
            else:
                _, added_utility = self.compute_best_white_die_choice(die[1])
                utilities[die[0]] = added_utility
        sorted_dice: List[Tuple[Color, int]] = [(c, v) for c, v in sorted(utilities.items(), key=lambda d: d[1])]
        sorted_dice.reverse()
        return sorted_dice

    def choose_die_wrapper(self, die, value) -> bool:
        """
        Wrapper function for attempting to choose either the white or a non-white die.
        :param die: The die color
        :param value: The value of the die
        :return: Whether or not the die was successfully chosen, as determined by the gamestate
        """
        if die == Color.WHITE:
            return self.game_state.choose_white_die(self.compute_best_white_die_choice(value)[0])
        else:
            return self.game_state.choose_die(die)
