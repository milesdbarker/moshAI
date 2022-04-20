""" Abstract module representing a gameplaying agent """
from typing import Dict

from abc import ABC, abstractmethod
from model.gamestate import GameState
from model.dice_colors import Color, get_all_colors


class Agent(ABC):
    """ Abstract class representing the state of one color on the game card """

    def __init__(self):
        self.game_state = GameState()
        # Keep tabs of how many times each color was chosen for this game
        self.colors_chosen = {color: 0 for color in get_all_colors()}

    @abstractmethod
    def choose_die(self, dice: Dict[Color, int]) -> Color:
        """
        Chooses and takes a die in the game state
        based on the algorithm implemented by this agent
        :param dice: The possible dice to choose from
        :return: The color die that was chosen (can be none)
        """

    # Runs the agent, printing the final score
    def run_agent(self) -> bool:
        print("Game starting")
        while not self.game_state.is_game_over():
            cur_dice = self.game_state.roll_dice()
            self.choose_die(cur_dice)
        print(f"Game over, final score: {self.game_state.get_utility()}")
        return True

    # Runs the agent, printing an action each time one is taken
    def run_agent_verbose(self) -> bool:
        print("Game starting")
        while not self.game_state.is_game_over():
            cur_dice = self.game_state.roll_dice()
            print(f"Dice rolled: {cur_dice}")
            die = self.choose_die(cur_dice)
            if die:
                print(f"Taking {die} {cur_dice[die]}")
            else:
                print("Skipping die")
        print(f"Game over, final score: {self.game_state.get_score()}")
        print(f"Colors chosen this game: {self.colors_chosen}")
        return True

    def compute_best_white_die_choice(self, value) -> Color:
        """
        Compute the best choice for the white die out of all possible colors.
        :param value: The value of the white die
        :return: The best color
        """
        utilities: Dict[Color, int] = {}
        for color in get_all_colors():
            if color == Color.WHITE:
                continue
            else:
                added_utility = self.game_state.card.get_utility([(color, value)]) - self.game_state.card.get_utility()
                utilities[color] = added_utility
        best_color = max(utilities.items(), key=lambda d: d[1])
        return best_color
