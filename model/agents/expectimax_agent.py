import itertools
from typing import Dict, List, Tuple
from itertools import product

from model.agents.abstract_agent import Agent
from model.gamestate import GameState
from model.scorecard import ScoreCard
from model.dice_colors import Color


class ExpectimaxAgent(Agent):

    # Pseudocode:
    # for each possible die, calculate the average end of turn expected utility
    # this will be 3*(6*6)*(2*6) calculations on the first die choice... may only work for our current model
    # calculations breakdown: dice choices * (next possible dice rolls given two dice) * (next
    # take the die with the highest

    # get choose_die to choose recursively
    # recursively choose based on the round number

    # This helper method will return the die that should be chosen given the possible dice, rolls left, and the scorecard
    # It will also return the expected utility at the end of the round if this die is taken
    def choose_die_helper(self, dice: Dict[Color, int], rolls_left: int, card: ScoreCard) -> (Color, int):
        dice_list = list(dice.keys())
        die_averages: {Color: int} = {}

        # TODO: Remove this and add white to the expectimax
        if Color.WHITE in dice_list:
            dice_list.remove(Color.WHITE)

        # Get the average utility of taking this die and the next possible role(s)
        for die_color in dice_list:
            card_copy = card.__copy__()
            # Skip invalid dice to save computation
            if not card_copy.add_die(die_color, dice[die_color]):
                continue
            # if this is the last roll, we don't have to choose a next die
            if rolls_left == 0:
                die_averages[die_color] = card_copy.get_utility()
            else:
                dice_expander = dice_list.copy()
                dice_expander.remove(die_color)
                # dice_expanded is a List[Tuple[Tuple[Color, int]]]. It is a list of ((Color, int)...) that contains
                # all the possible next rolls. Each inner Tuple is a dice roll while each outer Tuple is one possibility
                # of the next roll
                dice_expanded = dice_expansion(dice_expander, card_copy)
                avg = 0
                for dice_options in dice_expanded:
                    options = list(dice_options)
                    next_dice: {Color: int} = {}
                    for col, val in options:
                        next_dice[col] = val
                    util = self.choose_die_helper(next_dice, rolls_left - 1, card_copy.__copy__())[1]
                    avg += util
                avg = avg / len(dice_expanded)
                die_averages[die_color] = avg
        while True:
            if len(die_averages) == 0:
                return None, card.get_utility()
            max_avg = max(die_averages, key=die_averages.get)
            if card.add_die(max_avg, dice[max_avg]):
                return max_avg, die_averages[max_avg]
            else:
                die_averages.pop(max_avg)

    def choose_die(self, dice: Dict[Color, int]) -> Color:
        die = self.choose_die_helper(dice, (3 - self.game_state.roll_number), self.game_state.card.__copy__())[0]
        if die:
            self.game_state.choose_die(die)
        else:
            self.game_state.skip_choice()
        return die


def dice_expansion(dice_colors: List[Color], card: ScoreCard) -> List[Tuple[Tuple[Color, int]]]:
    dice_list = []
    for color in dice_colors:
        cur_list = []
        max_roll = 6 if color != Color.BLUE else 12
        for i in range(max_roll):
            if card.can_add_die(color, i + 1):
                cur_list.append((color, i + 1))
        dice_list.append(cur_list)
    dice_list = list(itertools.product(*dice_list))
    return dice_list
