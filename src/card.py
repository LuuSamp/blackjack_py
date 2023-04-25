from number import Number
from suit import Suit

class Card():
    def __init__(self, suit: Suit, number: Number):
        self.suit = suit
        self.number = number