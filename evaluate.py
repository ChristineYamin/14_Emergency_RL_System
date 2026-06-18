from environment import EmergencyEnvironment
from baseline import RandomAgent, GreedyAgent

def evaluate_random(num_episode=100):
    env = EmergencyEnvironment()
    agent = RandomAgent()

    total_reward = 0

    for _ in range(num_episode):
        env.reset()

        done = False

        while not done:
            action = agent.choose_action()
            _, reward, done = env.step(action)
            total_reward += reward
    return total_reward / num_episode

def evaluate_greedy(num_episodes=100):
    env = EmergencyEnvironment()
    agent = GreedyAgent()

    total_reward = 0

    for _ in range(num_episodes):
        env.reset()
        done = False
        while not done:
            action = agent.choose_action(
                env.ambulance_pos,
                env.emergency_pos
            )
            _, reward, done = env.step(action)
            total_reward += reward
    return total_reward / num_episodes

random_score = evaluate_random()
greedy_score = evaluate_greedy()

print("\n---------Baseline Results----------")
print(f"Random Agent Avg Reward : {random_score:.2f}")
print(f"Greedy Agent Avg Reward : {greedy_score:.2f}")