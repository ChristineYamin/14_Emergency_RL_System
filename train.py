from environment import EmergencyEnvironment
from agent import QLearningAgent
import pandas as pd

# Create environment and agent
env = EmergencyEnvironment()
agent = QLearningAgent()

# Training settings
episodes = 1000

# Store rewards for plotting
episode_rewards = []

# Training loop
for episode in range(episodes):

    state = env.reset()

    done = False
    total_reward = 0

    while not done:

        # Agent chooses action
        action = agent.choose_action(state)

        # Environment responds
        next_state, reward, done = env.step(action)

        # Agent learns
        agent.update(
            state,
            action,
            reward,
            next_state
        )

        state = next_state

        total_reward += reward

    # Save reward for this episode
    episode_rewards.append(total_reward)

    # Print progress every 100 episodes
    if episode % 100 == 0:
        print(
            f"Episode {episode} | Reward: {total_reward}"
        )

print("Training Finished!")

# Save results to CSV
df = pd.DataFrame({
    "Episode": range(len(episode_rewards)),
    "Reward": episode_rewards
})

df.to_csv("training_results.csv", index=False)

print("Results saved to training_results.csv")

# Show last 10 rewards
print("\nLast 10 Episode Rewards:")
print(episode_rewards[-10:])