from model.agents.expectimax_agent import ExpectimaxAgent
from model.agents.random_agent import RandomAgent

agent1 = ExpectimaxAgent()
agent1.run_agent_verbose()

agent2 = RandomAgent()
agent2.run_agent()
