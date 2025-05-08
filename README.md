# Advanced Probability-Based Games in Python

A collection of sophisticated probability simulations and statistical games implemented in Python. These projects demonstrate advanced concepts like Bayesian statistics, Markov chains, Monte Carlo methods, reinforcement learning, and epidemiological modeling.

## Contents

1. [Bayesian Dice Game](#bayesian-dice-game)
2. [Markov Chain Text Generator](#markov-chain-text-generator)
3. [Monte Carlo Stock Simulator](#monte-carlo-stock-simulator)
4. [Reinforcement Learning Bandit](#reinforcement-learning-bandit)
5. [Poker Probability Calculator](#poker-probability-calculator)

## Bayesian Dice Game

**File:** `bayesian_dice.py`

A game that demonstrates Bayesian probability updating as you observe dice rolls.

```python
# Example output:
Initial probabilities: {'D4': 0.333, 'D6': 0.333, 'D8': 0.333}
Rolled: 3, Updated probs: {'D4': 0.4, 'D6': 0.4, 'D8': 0.2}
Rolled: 6, Updated probs: {'D4': 0.0, 'D6': 0.8, 'D8': 0.2}
Rolled: 2, Updated probs: {'D4': 0.0, 'D6': 1.0, 'D8': 0.0}

# Example output (trained on Shakespeare):
"To be or not to be that is the question whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune"

# Example output (trained on tech articles):
"The neural network architecture uses multiple hidden layers with dropout regularization to prevent overfitting during the training phase"

Expected Price: $108.32
5% VaR: $82.15
95% VaR: $141.76

After 1000 steps:
Average Reward: 1.42
Optimal Action %: 85.3%

# Example output:
Win probability with ['A♠', 'K♥']: 49.37%
Win probability with ['7♣', '2♦']: 12.85%
Win probability with ['A♠', 'A♥']: 83.91%

#final output
![image](https://github.com/user-attachments/assets/56bd994f-13f4-4302-a531-d9d3229a611d)

![image](https://github.com/user-attachments/assets/f2bfbd68-8943-4740-9918-ae19423a9e6e)

![image](https://github.com/user-attachments/assets/d2a15e91-2a3e-4c1c-993e-7680c20a00e5)
![image](https://github.com/user-attachments/assets/cb0eab97-4d19-4019-ab85-a68afda3bd48)

![image](https://github.com/user-attachments/assets/7a1251ed-8069-4599-bb82-9d260c46ae90)

![image](https://github.com/user-attachments/assets/ffbdda50-f89f-4c5e-be5c-221cc99d7065)



Requirements
Python 3.8+

numpy

matplotlib

scipy

pandas (for stock simulator)
