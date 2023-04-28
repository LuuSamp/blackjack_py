from enum import Enum

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4
    
    def __str__(self):
        match self:
            case Suit.HEARTS: return "HEARTS"
            case Suit.DIAMONDS: return "DIAMONDS"
            case Suit.SPADES: return "SPADES"
            case Suit.CLUBS: return "CLUBS"