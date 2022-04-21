from typing import Dict, Tuple, List
from model.agents.abstract_agent import Agent
from model.dice_colors import Color


class ManualAgent(Agent):

    def choose_die(self, dice: Dict[Color, int]) -> Color:
        color_scores = self.game_state.card.get_color_scores()
        print(f"Current color scores: {color_scores}")
        dice_roll_valid: List[Tuple[str, int, str]] = []
        for die, value in dice.items():
            if die != Color.WHITE:
                valid = "Can take" if self.game_state.card.can_add_die(die, value) else "Cannot take"
                dice_roll_valid.append((die.value, value, valid))
            else:
                dice_roll_valid.append((die.value, value, "Can take"))
        print(f"Current dice roll: {dice_roll_valid}")
        print("Please enter the color of the die you would like to choose or skip")
        while True:
            color = input().upper()
            if color == "SKIP":
                self.game_state.skip_choice()
                return None
            if hasattr(Color, color):
                if color.lower() == Color.WHITE.value:
                    print("Please enter the color you would like to use the white die as:")
                    color = input().upper()
                    if not hasattr(Color, color) or color.lower() == Color.WHITE.value \
                            or not self.game_state.choose_white_die(Color(color.lower())):
                        print("Please rechoose and use a valid color for the white die")
                        continue
                    else:
                        die = Color(color.lower())
                        self.colors_chosen[die] += 1
                        return die
                elif self.game_state.choose_die(Color(color.lower())):
                    die = Color(color.lower())
                    self.colors_chosen[die] += 1
                    return die
                else:
                    print("That color cannot be taken, please choose a different one")
            else:
                print("That is not a valid die color, please try again")
