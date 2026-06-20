from environment import EmergencyEnvironment
from agent import QLearningAgent
import pickle

env = EmergencyEnvironment()
agent = QLearningAgent()

with open("q_table.pkl", "rb") as f:
    agent.q_table = pickle.load(f)

agent.epsilon = 0

total_reward = 0
episodes = 100

for _ in range(episodes):

    state = env.reset()
    done = False

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        total_reward += reward

        state = next_state

avg_reward = total_reward / episodes

print(f"Q-Learning Avg Reward: {avg_reward:.2f}")