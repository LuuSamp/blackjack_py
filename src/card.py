from number import Number
from suit import Suit

class Card():
    def __init__(self, suit: Suit, number: Number):
        self.suit = suit
        self.number = number
    
    def __eq__(self, other):
        if not isinstance(other, self):
            return False
        
        return self.suit == other.suit and self.number == other.number