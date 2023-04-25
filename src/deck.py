from number import Number
from suit import Suit
from card import Card

class Deck():
    def __init__(self):
        self.deck = []
        for suit in Suit:
            for number in Number:
                self.deck.append(Card(suit, number))
    
    def remove_card(self, card:Card):
        for i in range(len(self.deck)):
            if card == self.deck[i]:
                self.deck.pop(i)