import numpy as np
import numpy.typing as npt
from typing import Any

from card import Card

class FaceDownDeck:
    def __init__(self, num_decks: int = 1) -> None:
        
        if num_decks < 0:
            raise ValueError('A deck must be empty, or contain one or more copies')
        
        base_deck: npt.NDArray[np.object_] = np.array([Card(r + 1, s) for s in 'HSDC' for r in range(13)])
        
        self._deck: npt.NDArray[np.object_] = np.tile(base_deck, num_decks)
    
    def shuffle(self) -> None:
        np.random.shuffle(self._deck)
        
    
    def show(self) -> None:
        transform_deck = np.vectorize(str)
        print(self._deck if self.is_empty() else transform_deck(self._deck))
    
    
    def draw_top(self, num_cards: int = 1) -> npt.NDArray[np.object_] | None:
        if len(self) - num_cards < 0:
            raise ValueError('Cannot draw more cards than are left in the deck')
        
        drawn, self._deck = self._deck[:num_cards], self._deck[num_cards:]
        return drawn
    
    
    def draw_bottom(self, num_cards: int = 1) -> npt.NDArray[np.object_] | None:
        if len(self) - num_cards < 0:
            raise ValueError('Cannot draw more cards than are left in the deck')
                 
        num_cards -= 1
        drawn, self._deck = self._deck[~num_cards:], self._deck[:~num_cards]
        return drawn
    
    
    def push_top(self, cards: npt.NDArray[np.object_]) -> None:
        self._deck = np.insert(self._deck, 0, cards)
    
    
    def push_bottom(self, cards: npt.NDArray[np.object_]) -> None:
        self._deck = np.insert(self._deck, len(self), cards)
    
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    
    def __len__(self) -> int:
        return len(self._deck)
    
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, FaceDownDeck):
            return np.array_equal(self._deck, other._deck)
        return False


class FaceUpDeck(FaceDownDeck):
    def __init__(self, num_decks: int = 1) -> None:
        super().__init__(num_decks)
    
    def peek(self) -> Card: # Maybe change to peek the top n cards
        return self._deck[0] # Returns a view of the deck, can alter the deck externally. FIX
    
    def peek_deck(self) -> npt.NDArray[np.object_]:
        return self._deck.copy()