from number import Number
from suit import Suit
from card import Card
from deck import Deck

class Player:
    def __init__(self, name:str):
        self.name = name
        self.cards = []
        self.ingame = True
        
    def take_card(self, card:Card):
        self.cards.append(card)
    
    def score(self):
        return sum([int(i) for i in self.cards])
    

if __name__=="__main__":
    player = Player('Jorge')
    player.take_card(Card(Suit.SPADES, Number.ACE))
    print(player.score())
    player.take_card(Card(Suit.HEARTS, Number.QUEEN))
    print(player.score())  