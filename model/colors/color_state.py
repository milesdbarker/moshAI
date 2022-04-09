""" Abstract module representing the state of a color of the card """
from abc import ABC, abstractmethod
import copy
from typing import Optional


class ColorState(ABC):
    """ Abstract class representing the state of one color on the game card """

    @abstractmethod
    def add_die(self, die_result: int) -> bool:
        """
        Add the die to the color state. Returns true if the die could be added successfully, and false otherwise.
        :param die_result: The number of the colored die to add to the state
        :result: Whether or not adding the die was successful
        """

    @abstractmethod
    def is_next_die_valid(self, next: int) -> bool:
        """
        Determines if the next die is valid to add to this state.
        :param next: The result of the next die
        :return: Whether or not the die is valid and can be added to the state
        """

    @abstractmethod
    def get_utility(self, new_die: Optional[int] = None) -> int:
        """
        Get the utility of the state. If `new_die` is specified (not None), it will return the utility of the state
        if that die is added. Otherwise returns the utility of the state currently.
        :param new_die: The optional new die result to include in the utility calculation
        :return: The utility of the state
        """

    def copy_state(self):
        """
        Makes a deep copy of this color state
        :return: A ne copy of this color state
        """
        return copy.deepcopy(self)