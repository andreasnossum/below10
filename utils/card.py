from typing import Any

class Card:    
    def __init__(self, rank: int, suit: str) -> None:
        if rank - 1 not in range(13):
            raise ValueError('Not a valid rank, must be an integer from 1 to 13')
        
        if suit not in 'HSDC':
            raise ValueError('Not a valid suit, must be "H" (Hearts), "S" (Spades), "D" (Diamonds), or "C" (Clubs)')
        
        self.__rank_raw: int = rank
        self.__suit_raw: str = suit
        
        ranks: dict[int, str] = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        suits: dict[str, str] = {'H': 'Hearts', 'S': 'Spades', 'D': 'Diamonds'}
        
        self.__rank_special: str = ranks.get(rank, str(rank))
        self.__suit_special: str = suits.get(suit, 'Clubs')
    
    
    def show(self) -> None:
        print(f'{self.__rank_special} of {self.__suit_special}')
    
        
    def get_rank(self) -> int:
        return self.__rank_raw
    
    
    def get_suit(self) -> str:
        return self.__suit_raw
    
        
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Card):
            return self.get_rank() == other.get_rank() and self.get_suit() == other.get_suit()
        return False
    
        
    def __str__(self) -> str:
        return f'{self.__rank_raw}{self.__suit_raw}'