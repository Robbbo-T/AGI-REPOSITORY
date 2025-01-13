# Reinforcement Learning Algorithms in AGI-REPOSITORY

This document provides comprehensive information on the reinforcement learning algorithms used in the AGI-REPOSITORY project. It includes examples and explanations of Q-learning and policy gradient methods, and references the `src/learning/reinforcement_learning.py` file for implementation details.

## Q-Learning

Q-learning is a model-free reinforcement learning algorithm that aims to learn the value of an action in a particular state. The agent uses a Q-table to store the value of each state-action pair and updates the table based on the rewards received from the environment.

### Implementation

The Q-learning algorithm is implemented in the `QLearningAgent` class in the `src/learning/reinforcement_learning.py` file. Below is an example of how to use the `QLearningAgent` class:

```python
from src.learning.reinforcement_learning import QLearningAgent

# Define the state and action sizes
state_size = 10
action_size = 4

# Create a Q-learning agent
agent = QLearningAgent(state_size, action_size)

# Example of choosing an action and learning from a transition
state = 0
action = agent.choose_action(state)
reward = 1
next_state = 1
agent.learn(state, action, reward, next_state)
```

### Explanation

1. **Initialization**: The `QLearningAgent` class is initialized with the state size, action size, learning rate, discount factor, exploration rate, and exploration decay.
2. **Choosing an Action**: The `choose_action` method selects an action based on the exploration rate. If a random number is less than the exploration rate, a random action is chosen; otherwise, the action with the highest Q-value is selected.
3. **Learning from a Transition**: The `learn` method updates the Q-table based on the reward received and the next state. The Q-value for the current state-action pair is updated using the temporal difference (TD) error.

## Policy Gradient

Policy gradient methods aim to optimize the policy directly by adjusting the parameters of the policy based on the rewards received. The agent learns a probability distribution over actions for each state and updates the policy to maximize the expected reward.

### Implementation

The policy gradient algorithm is implemented in the `PolicyGradientAgent` class in the `src/learning/reinforcement_learning.py` file. Below is an example of how to use the `PolicyGradientAgent` class:

```python
from src.learning.reinforcement_learning import PolicyGradientAgent

# Define the state and action sizes
state_size = 10
action_size = 4

# Create a policy gradient agent
agent = PolicyGradientAgent(state_size, action_size)

# Example of choosing an action and storing a transition
state = 0
action = agent.choose_action(state)
reward = 1
agent.store_transition(state, action, reward)

# Learn from the stored transitions
agent.learn()
```

### Explanation

1. **Initialization**: The `PolicyGradientAgent` class is initialized with the state size, action size, and learning rate.
2. **Choosing an Action**: The `choose_action` method selects an action based on the probability distribution over actions for the given state.
3. **Storing a Transition**: The `store_transition` method stores the state, action, and reward for each transition.
4. **Learning from Transitions**: The `learn` method updates the policy based on the stored transitions. The policy is adjusted to increase the probability of actions that led to higher rewards.

## References

For more details on the implementation of these algorithms, refer to the `src/learning/reinforcement_learning.py` file in the AGI-REPOSITORY project.
