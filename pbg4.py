import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, k=10, epsilon=0.1):
        self.k = k
        self.epsilon = epsilon
        self.q_true = np.random.normal(0, 1, k)
        self.q_est = np.zeros(k)
        self.action_counts = np.zeros(k)
    
    def act(self):
        if np.random.random() < self.epsilon:
            return np.random.randint(self.k)  # Explore
        return np.argmax(self.q_est)  # Exploit
    
    def step(self, action):
        reward = np.random.normal(self.q_true[action], 1)
        self.action_counts[action] += 1
        self.q_est[action] += (reward - self.q_est[action]) / self.action_counts[action]
        return reward

# Simulation
bandit = Bandit(k=10, epsilon=0.1)
rewards = []
optimal_actions = []

for _ in range(1000):
    action = bandit.act()
    reward = bandit.step(action)
    rewards.append(reward)
    optimal_actions.append(action == np.argmax(bandit.q_true))

# Plot results
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(np.cumsum(rewards)/np.arange(1,1001), label='ε=0.1')
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()

plt.subplot(1,2,2)
plt.plot(np.cumsum(optimal_actions)/np.arange(1,1001), label='ε=0.1')
plt.xlabel('Steps')
plt.ylabel('% Optimal Action')
plt.legend()
plt.show()