from itertools import combinations
from collections import Counter
import random

# Card representations
suits = ['♠', '♥', '♦', '♣']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck = [r+s for s in suits for r in ranks]

def evaluate_hand(cards):
    """Return hand rank (simplified version)"""
    ranks = sorted(['2345678910JQKA'.index(c[:-1]) for c in cards], reverse=True)
    suits = [c[-1] for c in cards]
    
    # Check for flush
    flush = len(set(suits)) == 1
    
    # Check for straight
    straight = (max(ranks)-min(ranks)) == 4 and len(set(ranks)) == 5
    
    # Check for multiples
    counts = Counter(ranks)
    multiples = sorted(counts.values(), reverse=True)
    
    if straight and flush: return 8  # Straight flush
    if multiples[0] == 4: return 7  # Four of a kind
    if multiples == [3,2]: return 6  # Full house
    if flush: return 5               # Flush
    if straight: return 4            # Straight
    if multiples[0] == 3: return 3   # Three of a kind
    if multiples == [2,2,1]: return 2 # Two pair
    if multiples[0] == 2: return 1    # One pair
    return 0                          # High card

def monte_carlo_poker_prob(hole_cards, num_players=4, simulations=10000):
    deck_remaining = [c for c in deck if c not in hole_cards]
    wins = 0
    
    for _ in range(simulations):
        random.shuffle(deck_remaining)
        community = deck_remaining[:5]
        my_hand = hole_cards + community
        my_score = evaluate_hand(my_hand)
        
        opponents_best = 0
        for i in range(num_players-1):
            start = 5 + i*2
            opp_hole = deck_remaining[start:start+2]
            opp_hand = opp_hole + community
            opp_score = evaluate_hand(opp_hand)
            opponents_best = max(opponents_best, opp_score)
        
        if my_score > opponents_best:
            wins += 1
    
    return wins / simulations

# Example usage
hole_cards = ['A♠', 'K♥']
win_prob = monte_carlo_poker_prob(hole_cards)
print(f"Win probability with {hole_cards}: {win_prob*100:.2f}%")