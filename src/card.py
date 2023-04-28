from number import Number
from suit import Suit

class Card():
    def __init__(self, suit: Suit, number: Number):
        self.suit = suit
        self.number = number
    
    def __eq__(self, other):
        return self.suit == other.suit and self.number == other.number
    
    def __int__(self):
        return int(self.number)
    
    def __str__(self):
        return f"{self.number} {self.suit}"