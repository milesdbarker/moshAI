from model.agents.expectimax_agent import ExpectimaxAgent
from model.agents.greedy_agent import GreedyAgent
from model.agents.random_agent import RandomAgent
from model.agents.manual_agent import ManualAgent
from model.dice_colors import get_all_colors

# agent1 = ExpectimaxAgent()
# agent1.run_agent_verbose()

agent = ManualAgent()
agent.run_agent()

# r_scores = []
# r_colors_chosen = {color: 0 for color in get_all_colors()}
# for _ in range(0, 100):
#     agent2 = RandomAgent()
#     agent2.run_agent()
#     game_colors = agent2.colors_chosen
#     for color in game_colors.keys():
#         r_colors_chosen[color] += game_colors[color]
#     r_scores.append(agent2.game_state.get_score())
#
# g_scores = []
# g_colors_chosen = {color: 0 for color in get_all_colors()}
# for _ in range(0, 100):
#     agent3 = GreedyAgent()
#     agent3.run_agent()
#     game_colors = agent3.colors_chosen
#     for color in game_colors.keys():
#         g_colors_chosen[color] += game_colors[color]
#     g_scores.append(agent3.game_state.get_score())
#
# print("Random Agent Metrics")
# print(f"Min: {min(r_scores)}, Max: {max(r_scores)}, Average: {sum(r_scores) / len(r_scores)}")
# print(f"Color Stats: {r_colors_chosen}")

# print("Greedy Agent Metrics")
# print(f"Min: {min(g_scores)}, Max: {max(g_scores)}, Average: {sum(g_scores) / len(g_scores)}")
# print(f"Color Stats: {g_colors_chosen}")
