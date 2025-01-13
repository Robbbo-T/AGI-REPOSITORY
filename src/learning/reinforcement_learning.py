"""
Reinforcement Learning Algorithms for AGI-REPOSITORY
"""

import numpy as np
import unittest

class QLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.99, exploration_rate=1.0, exploration_decay=0.995):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.q_table = np.zeros((state_size, action_size))

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.action_size)
        return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state, best_next_action]
        td_error = td_target - self.q_table[state, action]
        self.q_table[state, action] += self.learning_rate * td_error
        self.exploration_rate *= self.exploration_decay

class PolicyGradientAgent:
    def __init__(self, state_size, action_size, learning_rate=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.states = []
        self.actions = []
        self.rewards = []
        self.policy = np.random.rand(state_size, action_size)

    def choose_action(self, state):
        probabilities = self.policy[state] / np.sum(self.policy[state])
        return np.random.choice(self.action_size, p=probabilities)

    def store_transition(self, state, action, reward):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)

    def learn(self):
        for state, action, reward in zip(self.states, self.actions, self.rewards):
            self.policy[state, action] += self.learning_rate * reward
        self.states = []
        self.actions = []
        self.rewards = []

def run_continuous_integration():
    class TestReinforcementLearning(unittest.TestCase):
        def setUp(self):
            self.q_agent = QLearningAgent(state_size=10, action_size=4)
            self.pg_agent = PolicyGradientAgent(state_size=10, action_size=4)

        def test_q_learning_agent(self):
            state = 0
            action = self.q_agent.choose_action(state)
            self.assertIn(action, range(4))
            self.q_agent.learn(state, action, reward=1, next_state=1)
            self.assertGreaterEqual(self.q_agent.q_table[state, action], 0)

        def test_policy_gradient_agent(self):
            state = 0
            action = self.pg_agent.choose_action(state)
            self.assertIn(action, range(4))
            self.pg_agent.store_transition(state, action, reward=1)
            self.pg_agent.learn()
            self.assertGreaterEqual(self.pg_agent.policy[state, action], 0)

    unittest.main()

if __name__ == "__main__":
    run_continuous_integration()
