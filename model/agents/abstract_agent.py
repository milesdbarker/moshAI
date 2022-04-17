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
        print(f"Game over, final score: {self.game_state.get_utility()}")
        print(f"Colors chosen this game: {self.colors_chosen}")
        return True
