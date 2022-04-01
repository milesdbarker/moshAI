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
            if self.game_state.choose_die(die):
                return die
        self.game_state.skip_choice()
        return None
