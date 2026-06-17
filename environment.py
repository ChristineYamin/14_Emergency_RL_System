import random


class EmergencyEnvironment:

    def __init__(self, grid_size=10):
        self.grid_size = grid_size

        self.ambulance_pos = None
        self.emergency_pos = None

        self.steps = 0
        self.max_steps = 100

    def reset(self):
        self.steps = 0

        self.ambulance_pos = (
            random.randint(0, self.grid_size - 1),
            random.randint(0, self.grid_size - 1)
        )

        self.emergency_pos = (
            random.randint(0, self.grid_size - 1),
            random.randint(0, self.grid_size - 1)
        )

        return self.get_state()

    def get_state(self):

        return (
            self.ambulance_pos[0],
            self.ambulance_pos[1],
            self.emergency_pos[0],
            self.emergency_pos[1]
        )
    
    def step(self, action):

        self.steps += 1
        x, y = self.ambulance_pos

        if action == 0:  # UP
            x -= 1
        
        elif action == 1:  # Down
            x += 1

        elif action == 2:  # Left
            y -= 1
        
        elif action == 3:  # Right
            y += 1
        
        # Keep ambulance inside grid
        x = max(0, min(x, self.grid_size - 1))
        y = max(0, min(y, self.grid_size - 1))

        self.ambulance_pos = (x,y)

        # Reward System
        if self.ambulance_pos == self.emergency_pos:
            reward = 100
            done = True
        elif self.steps >= self.max_steps:
            reward = -100
            done = True
            
        else:
            reward = -1
            done = False

        return self.get_state(), reward, done
    
if __name__ == "__main__":

    env = EmergencyEnvironment()

    state = env.reset()

    print("Ambulance:", env.ambulance_pos)
    print("Emergency:", env.emergency_pos)

    done = False

    while not done:
        action = random.randint(0,3)

        next_state, reward, done = env.step(action)
        print(
            f"Position: {env.ambulance_pos}, "
            f"Reward: {reward}, "
            f"Done: {done}"
        )