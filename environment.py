import random


class EmergencyEnvironment:

    def __init__(self, grid_size=10):
        self.grid_size = grid_size

        self.ambulance_pos = None
        self.emergency_pos = None

        self.steps = 0
        self.max_steps = 100

        self.num_obstacles = 10
        self.obstacles = []

        self.num_traffic_zones = 5
        self.traffic_zones = []

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

        self.obstacles = []
        while len(self.obstacles) < self.num_obstacles:
            obstacle = (
                random.randint(0, self.grid_size - 1),
                random.randint(0, self.grid_size - 1)
            )

            if (
                obstacle != self.ambulance_pos
                and obstacle != self.emergency_pos
                and obstacle not in self.obstacles
            ):
                self.obstacles.append(obstacle)
        
        self.traffic_zones = []
        while len(self.traffic_zones) < self.num_traffic_zones:
            zone = (
                random.randint(0, self.grid_size - 1),
                random.randint(0, self.grid_size - 1)
            )

            if (
                zone != self.ambulance_pos
                and zone != self.emergency_pos
                and zone not in self.obstacles
                and zone not in self.traffic_zones
            ):
                self.traffic_zones.append(zone)
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

        new_position = (x,y)
        if new_position not in self.obstacles:
            self.ambulance_pos = new_position
        
        if new_position in self.obstacles:
            reward = -10
            done = False
            return self.get_state(), reward, done
        
        if self.ambulance_pos in self.traffic_zones:
            reward = -6
            done = False
            return self.get_state(), reward, done
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
    
    print("Obstacles:", env.obstacles)
    print("Traffic Zones:", env.traffic_zones)