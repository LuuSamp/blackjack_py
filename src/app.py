from number import Number
from suit import Suit
from card import Card
from deck import Deck
from player import Player
    

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

def in_game(player:Player):
    if player.ingame: return True
    
    return False

def leave_game(player:Player):
    player.ingame = False

def game_over(players):
    for player in players:
        if player.ingame == True: return False
        
    return True

def draw():
    answer = input(f"Do you want to draw a card? Y/N\n")
    while True:
        if answer == 'Y': return True
        if answer == 'N': return False
        answer = input("Answer with Y for YES or N for NO!\n")

def main():
    players, deck = start()
    i = -1
    while not game_over(players):
        i += 1
        if i == len(players): i = 0
        print(f"\n{players[i].name}\'s turn")
        if not draw():
            players[i].ingame = False
            continue
        card = deck.get_random()
        print(f"{players[i].name} has drawn {card}")