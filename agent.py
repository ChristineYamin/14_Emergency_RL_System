import random

class QLearningAgent:
    def __init__(self):
        self.q_table = {}

        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def get_q_values(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0, 0, 0, 0]
        return self.q_table[state]
    
    def choose_action(self, state):

        q_values = self.get_q_values(state)

        if random.random() < self.epsilon:
            return random.randint(0, 3)

        return q_values.index(max(q_values))
    
    def update(self, state, action, reward, next_state):

        current_q = self.get_q_values(state)[action]

        max_next_q = max(self.get_q_values(next_state))

        new_q = current_q + self.alpha * (
            reward + self.gamma * max_next_q - current_q
        )

        self.q_table[state][action] = new_q
    
if __name__ == "__main__":

    agent = QLearningAgent()

    state = (1, 2, 3, 4)
    next_state = (1, 3, 3, 4)

    action = 3
    reward = 100

    agent.update(
        state,
        action,
        reward,
        next_state
    )

    print(agent.q_table)