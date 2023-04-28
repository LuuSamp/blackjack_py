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
    print()
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
    return True
    
def exceed(player:Player):
    leave_game(player)
    player.exceeded = True
    return True

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

def player_draw(deck:Deck, player:Player):
    card = deck.get_random()
    player.take_card(card)
    deck.remove_card(card)
    return card

def main():
    players, deck = start()
    i = -1
    while not game_over(players):
        i += 1
        if i == len(players): i = 0
        if not in_game(players[i]): continue
        
        name = players[i].name
        print(f"{name}\'s turn")
        
        if not draw():
            players[i].ingame = False
            print()
            continue
        print()
        
        card = player_draw(deck, players[i])
        
        print(f"{name} has drawn {card}, of value {int(card.number)}")
        print(f"{name}'s cards: {[str(players[i].cards[c]) for c in range(len(players[i].cards))]}")
        print(f"{name}'s current score: {players[i].score()}")
        
        if players[i].score() > 21:
            exceed(players[i])
            print(f"{name} exceeded 21 and is out of game")
        print()
    
    bscore = 0
    for player in players:
        if player.exceeded:
            continue
        if player.score() > bscore:
            bscore = player.score()
            winner = player
    print(f"{winner.name} won! \n")
        
        
if __name__ == "__main__":
    main()