from number import Number
from suit import Suit
from card import Card
from deck import Deck

class Player:
    def __init__(self, name:str):
        self.name = name
        self.cards = []
        
    def take_card(self, card:Card):
        self.cards.append(card)
        