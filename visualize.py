import pandas as pd
import matplotlib.pyplot as plt

# Load training results
df = pd.read_csv("training_results.csv")

# Moving average over 50 episodes
df["Moving_Avg"] = df["Reward"].rolling(window=50).mean()

# Create figure
plt.figure(figsize=(10, 5))

# Plot rewards
plt.plot(df["Episode"], df["Reward"], alpha=0.3, label="Reward")
plt.plot(df["Episode"], df["Moving_Avg"], linewidth=3, label="50-Episode Moving Average")

# Labels
plt.title("Emergency Response RL Training Performance")
plt.xlabel("Episode")
plt.ylabel("Reward")

# Grid
plt.legend()
plt.grid(True)

# Show chart
plt.show()