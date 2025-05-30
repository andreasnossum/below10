# Class to handle cards on hand

# Functionalitites: (suggestion)
# - draw(): draw one card from deck (or face-up pile?) --> correlate with cards in deck
# - play(): play one card from hand --> correlate with cards in deck

import numpy as np

class Hand:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def highest_card(self):

        ranks = np.array([card.get_rank() for card in self.hand])
        ranks_max = ranks.max()
        return self.hand[ranks == ranks_max]
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def __len__(self) -> int:
        return len(self.hand)
    


    

