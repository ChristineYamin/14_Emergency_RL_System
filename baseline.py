import random

class RandomAgent:
    def choose_action(self):
        return random.randint(0,3)
    
class GreedyAgent:
    def choose_action(
            self,
            ambulance_pos,
            emergency_pos
    ):
        ax, ay = ambulance_pos
        ex, ey = emergency_pos

        # Move vertically first
        if ax < ex:
            return 1 # Down
        
        if ax > ex:
            return 0 # Up
        
        # Move horizontally
        if ay < ey:
            return 3 # Right
        
        if ay > ey:
            return 2 # Left
        
        return 0

if __name__ == "__main__":

    greedy = GreedyAgent()

    ambulance = (2, 3)
    emergency = (7, 3)

    action = greedy.choose_action(
        ambulance,
        emergency
    )

    print("Action:", action)