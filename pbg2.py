import random
from collections import defaultdict

class MarkovChain:
    def __init__(self, order=2):
        self.order = order
        self.chain = defaultdict(list)
    
    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.order):
            state = tuple(words[i:i+self.order])
            next_word = words[i+self.order]
            self.chain[state].append(next_word)
    
    def generate(self, length=50):
        current = random.choice(list(self.chain.keys()))
        output = list(current)
        
        for _ in range(length):
            if current not in self.chain:
                break
            next_word = random.choice(self.chain[current])
            output.append(next_word)
            current = tuple(output[-self.order:])
        
        return ' '.join(output)

# Example usage
text = """The quick brown fox jumps over the lazy dog. The dog barks at the fox. 
          The fox runs away from the dog. The dog chases the fox."""
          
markov = MarkovChain(order=2)
markov.train(text)
print(markov.generate(length=20))