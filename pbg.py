import numpy as np
from collections import defaultdict

class BayesianDice:
    def __init__(self, dice_types):
        self.dice_types = dice_types  # Format: {'D6': [1,2,3,4,5,6], 'D20': [...], ...}
        self.prior = {name: 1/len(dice_types) for name in dice_types}
        self.roll_history = []
    
    def roll(self):
        # Select dice based on current probabilities
        chosen = np.random.choice(list(self.prior.keys()), p=list(self.prior.values()))
        outcome = np.random.choice(self.dice_types[chosen])
        self.roll_history.append(outcome)
        
        # Update probabilities using Bayes' theorem
        for dice in self.prior:
            likelihood = outcome in self.dice_types[dice]
            self.prior[dice] *= likelihood * len(self.dice_types[dice])
        
        # Normalize
        total = sum(self.prior.values())
        self.prior = {k: v/total for k, v in self.prior.items()}
        
        return outcome
    
    def get_probabilities(self):
        return self.prior

# Example usage
dice = {
    'D4': [1,2,3,4],
    'D6': [1,2,3,4,5,6],
    'D8': [1,2,3,4,5,6,7,8]
}

game = BayesianDice(dice)
print("Initial probabilities:", game.get_probabilities())

for _ in range(10):
    roll = game.roll()
    print(f"Rolled: {roll}, Updated probs:", {k: round(v, 3) for k, v in game.get_probabilities().items()})