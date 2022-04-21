from model.agents.expectimax_agent import ExpectimaxAgent
from model.agents.greedy_agent import GreedyAgent
from model.agents.random_agent import RandomAgent
from model.agents.manual_agent import ManualAgent
from model.dice_colors import get_all_colors

# agent1 = ExpectimaxAgent()
# agent1.run_agent_verbose()


def run_manual_batch(num_games: int):
    m_scores = []
    m_colors_chosen = {color: 0 for color in get_all_colors()}
    for _ in range(0, num_games):
        agent = ManualAgent()
        agent.run_agent()
        game_colors = agent.colors_chosen
        for color in game_colors.keys():
            m_colors_chosen[color] += game_colors[color]
        m_scores.append(agent.game_state.get_score())
    print("Manual Agent Metrics")
    print(f"Min: {min(m_scores)}, Max: {max(m_scores)}, Average: {sum(m_scores) / len(m_scores)}")
    print(f"Color Stats: {m_colors_chosen}")


def run_random_batch(num_games: int):
    r_scores = []
    r_colors_chosen = {color: 0 for color in get_all_colors()}
    for _ in range(0, num_games):
        agent2 = RandomAgent()
        agent2.run_agent()
        game_colors = agent2.colors_chosen
        for color in game_colors.keys():
            r_colors_chosen[color] += game_colors[color]
        r_scores.append(agent2.game_state.get_score())
    print("Random Agent Metrics")
    print(f"Min: {min(r_scores)}, Max: {max(r_scores)}, Average: {sum(r_scores) / len(r_scores)}")
    print(f"Color Stats: {r_colors_chosen}")


def run_greedy_batch(num_games: int):
    g_scores = []
    g_colors_chosen = {color: 0 for color in get_all_colors()}
    for _ in range(0, num_games):
        agent3 = GreedyAgent()
        agent3.run_agent()
        game_colors = agent3.colors_chosen
        for color in game_colors.keys():
            g_colors_chosen[color] += game_colors[color]
        g_scores.append(agent3.game_state.get_score())
    print("Greedy Agent Metrics")
    print(f"Min: {min(g_scores)}, Max: {max(g_scores)}, Average: {sum(g_scores) / len(g_scores)}")
    print(f"Color Stats: {g_colors_chosen}")


run_manual_batch(3)


