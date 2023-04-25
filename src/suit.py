from enum import Enum

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4
    
    def __str__(self):
        match self:
            case Suit.HEARTS: "HEARTS"
            case Suit.DIAMONDS: "DIAMONDS"
            case Suit.SPADES: "SPADES"
            case Suit.CLUBS: "CLUBS"