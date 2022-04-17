from typing import Dict
import random

from model.agents.abstract_agent import Agent
from model.gamestate import GameState
from model.dice_colors import Color


class RandomAgent(Agent):

    def choose_die(self, dice: Dict[Color, int]) -> Color:
        dice_list = list(dice.keys())
        random.shuffle(dice_list)
        for die in dice_list:
            if die == Color.WHITE:
                dice_list_copy = dice_list.copy()
                dice_list_copy.remove(Color.WHITE)
                random.shuffle(dice_list_copy)
                if self.game_state.choose_white_die(dice_list_copy[0]):
                    self.colors_chosen[die] += 1
                    return die
            elif self.game_state.choose_die(die):
                self.colors_chosen[die] += 1
                return die
        self.game_state.skip_choice()
        return None
