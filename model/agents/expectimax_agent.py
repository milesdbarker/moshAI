import itertools
from typing import Dict, List
from itertools import product

from model.agents.abstract_agent import Agent
from model.gamestate import GameState
from model.dice_colors import Color


class ExpectimaxAgent(Agent):

    # Pseudocode:
    # for each possible die, calculate the average end of turn expected utility
    # this will be 3*(6*6)*(2*6) calculations on the first die choice... may only work for our current model
    # calculations breakdown: dice choices * (next possible dice rolls given two dice) * (next
    # take the die with the highest

    def choose_die(self, game_state: GameState, dice: Dict[Color, int]) -> Color:
        self.game_state._turn_number = 6
        dice_list = list(dice.keys())
        die_averages: [(Color, int)] = []
        for die_color in dice_list:
            dice_expander = dice_list.copy()
            dice_expander.remove(die_color)
            dice_expanded = dice_expansion(dice_expander)
            game_copy = game_state.copy()
            print(dice_expanded)
        self.game_state.skip_choice()
        return None


def dice_expansion(dice_colors: List[Color]) -> List[List[Dict[Color, int]]]:
    dice_list = []
    for color in dice_colors:
        cur_list = []
        for i in range(6):
            cur_list.append([(color, i + 1)])
        dice_list.append(cur_list)
    dice_list = list(itertools.product(*dice_list))
    return dice_list
