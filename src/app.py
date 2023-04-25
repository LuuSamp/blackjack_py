from number import Number
from suit import Suit
from card import Card
from deck import Deck
from player import Player
    
def init_deck():
    return Deck()

def init_players(quant:int):
    players = []
    for i in range(quant):
        name = input(f"Name of player {i+1}: ")
        players.append(Player(name))
    
    return players

def start():
    quant = int(input("Quantity of players: "))
    players = init_players(quant)
    deck = Deck()
    return players, deck


if __name__ == "__main__":
    players, deck = start()