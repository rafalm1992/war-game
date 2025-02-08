import random
from enum import Enum

class Player:
    def __init__(self, name, cards_deck, playground):
        self.name = name
        self.cards_deck = cards_deck
        self.playground = playground
        
    def put_card_into_playground(self): 
        card = self.cards_deck.pop(0)
        self.playground.add_cards_to_play_pile([card])
        return card
    
    def put_three_cards_into_playground(self):
        cards = [self.cards_deck.pop(0) for _ in range(3)]
        self.playground.add_cards_to_play_pile(cards)
    
    def take_won_cards_from_play_pile(self):
        won_cards = self.playground.return_cards_from_pile_and_reset_play_pile()
        self.cards_deck.extend(won_cards)
    
    def __str__(self):
        return f"Name: {self.name}, cards: {self.cards}"
    
class Playground:
    def __init__(self):
        self.play_pile = []
        
    def add_cards_to_play_pile(self, cards):
        self.play_pile.extend(cards)
        
    def return_cards_from_pile_and_reset_play_pile(self):
        cards = self.play_pile
        self.play_pile = []
        return cards

class MatchType(Enum):
    BATTLE = "battle"
    WAR = "war"

    
def generate_shuffled_deck():
    cards_deck = []
    for i in ["Heart", "Diamond", "Club", "Spade"]:
        for index, j in enumerate(["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]):
            cards_deck.append({"card": [j, i], "value": index})
    random.shuffle(cards_deck)
    return cards_deck
    
def split_deck_into_two_halves(lst):
    mid = len(lst) // 2  
    return lst[:mid], lst[mid:]  # Split into two halves

def format_card(card):
    suit_emoji = card['card'][1].replace("Heart", "\u2764\ufe0f") \
                            .replace("Spade", "\u2660\ufe0f") \
                            .replace("Club", "\u2663\ufe0f") \
                            .replace("Diamond", "\u2666\ufe0f")
    return f"{card['card'][0]} {suit_emoji}"

def check_if_player_has_enough_cards_to_play(player1, player2, minimum_amount_of_cards_to_play):
    if len(player1.cards_deck) < minimum_amount_of_cards_to_play:
        print(f"{player1.name} has not enough cards. {player2.name} WINS THE GAME!")
        return False
    if len(player2.cards_deck) < minimum_amount_of_cards_to_play:
        print(f"{player2.name} has not enough cards. {player1.name} WINS THE GAME!")
        return False
    return True

# def generate_card_message(card):
#     return print(format_card(card))

def generate_winner_loser_message(winner, winner_card, loser, loser_card, type_of_match):
    message = (
        "\n"+ "#" * 50 + "\n" +
        f"\n{format_card(winner_card)} is higher than {format_card(loser_card)}\n" +
        f"\n{winner.name} won the {type_of_match.value} and {loser.name} lost it \n" + "\n" +
        "#" * 50 
        +"\n"
    )
    return print(message)

def print_three_empty_cards():
    
    card_art = [
        "┌───┐"*3,
        "│   │"*3,
        "│   │"*3,
        "└───┘"*3
    ]
    
    for line in card_art:
        print(line)

def print_card(card):
    
    rank, suit = card["card"]
    
    
    # Mapping suit names to symbols
    suit_symbols = {
        "Heart": "\u2764\ufe0f",
        "Diamond": "\u2666\ufe0f",
        "Club": "\u2663\ufe0f",
        "Spade": "\u2660\ufe0f"
    }
    
    suit_symbol = suit_symbols.get(suit, "?")  # Default to "?" if suit not found

    # Ensure rank is always 2 characters for alignment (e.g., "10" vs "K ")
    rank = rank[0] + " " if rank == "10" else rank[0] + " "

    card_art = [
        "┌───┐",
        f"│{rank} │",
        f"│ {suit_symbol} │",
        "└───┘"
    ]
    
    for line in card_art:
        print(line)


def main():
    half_deck_1, half_deck_2 = split_deck_into_two_halves(generate_shuffled_deck())
    # half_deck_1 = [{'card': ['King', 'Club'], 'value': 11}, {'card': ['10', 'Diamond'], 'value': 8}, {'card': ['Ace', 'Diamond'], 'value': 12}, {'card': ['8', 'Heart'], 'value': 6}, {'card': ['7', 'Club'], 'value': 5}, {'card': ['4', 'Spade'], 'value': 2}, {'card': ['4', 'Diamond'], 'value': 2}, {'card': ['Queen', 'Club'], 'value': 10}, {'card': ['7', 'Spade'], 'value': 5}, {'card': ['7', 'Diamond'], 'value': 5}, {'card': ['8', 'Spade'], 'value': 6}, {'card': ['9', 'Diamond'], 'value': 7}, {'card': ['6', 'Diamond'], 'value': 4}, {'card': ['4', 'Club'], 'value': 2}, {'card': ['Jack', 'Diamond'], 'value': 9}, {'card': ['7', 'Heart'], 'value': 5}, {'card': ['King', 'Spade'], 'value': 11}, {'card': ['6', 'Heart'], 'value': 4}, {'card': ['6', 'Club'], 'value': 4}, {'card': ['10', 'Spade'], 'value': 8}, {'card': ['3', 'Diamond'], 'value': 1}, {'card': ['8', 'Diamond'], 'value': 6}, {'card': ['10', 'Heart'], 'value': 8}, {'card': ['Jack', 'Club'], 'value': 9}, {'card': ['Ace', 'Club'], 'value': 12}, {'card': ['5', 'Heart'], 'value': 3}]
    # half_deck_2 = [{'card': ['King', 'Club'], 'value': 11}, {'card': ['10', 'Diamond'], 'value': 8}, {'card': ['Ace', 'Diamond'], 'value': 12}, {'card': ['8', 'Heart'], 'value': 6}, {'card': ['7', 'Club'], 'value': 5}, {'card': ['4', 'Spade'], 'value': 2}, {'card': ['4', 'Diamond'], 'value': 2}, {'card': ['Queen', 'Club'], 'value': 10}, {'card': ['7', 'Spade'], 'value': 5}, {'card': ['7', 'Diamond'], 'value': 5}, {'card': ['8', 'Spade'], 'value': 6}, {'card': ['9', 'Diamond'], 'value': 7}, {'card': ['6', 'Diamond'], 'value': 4}, {'card': ['4', 'Club'], 'value': 2}, {'card': ['Jack', 'Diamond'], 'value': 9}, {'card': ['7', 'Heart'], 'value': 5}, {'card': ['King', 'Spade'], 'value': 11}, {'card': ['6', 'Heart'], 'value': 4}, {'card': ['6', 'Club'], 'value': 4}, {'card': ['10', 'Spade'], 'value': 8}, {'card': ['3', 'Diamond'], 'value': 1}, {'card': ['8', 'Diamond'], 'value': 6}, {'card': ['10', 'Heart'], 'value': 8}, {'card': ['Jack', 'Club'], 'value': 9}, {'card': ['Ace', 'Club'], 'value': 12}, {'card': ['5', 'Heart'], 'value': 3}]
    players = []
    first_player = input("Enter first player name: ")
    second_player = input("Enter second player name: ")
    players = [first_player, second_player]
    random.shuffle(players)
    print(f"{"✧✩✫✮✯✮✫✩✧"*8}")
    print(f"\n{players[0]} starts the game!\n")
    print(f"{"✧✩✫✮✯✮✫✩✧"*8}")

    playground = Playground()

    player1 = Player(players[0], half_deck_1, playground)
    player2 = Player(players[1], half_deck_2, playground)

    # print(player1)
    # print(player2)
    # player1_first_card_from_deck = player1.cards.pop(0)
    # player2_first_card_from_deck = player2.cards.pop(0)
    # print(player1_first_card_from_deck['value'])
    # print(player2_first_card_from_deck['value'])
    
    play_battle(player1, player2)

    

    
def play_battle(player1, player2):
    if not check_if_player_has_enough_cards_to_play(player1, player2, 1): return 
    while True:
        if not check_if_player_has_enough_cards_to_play(player1, player2, 1): return 
        input(f"{player1.name}, it's your turn, click Enter to put card on playground")
        player1_first_card_from_deck = player1.put_card_into_playground()
        print_card(player1_first_card_from_deck)
        input(f"{player2.name}, it's your turn, click Enter to put card on playground")
        player2_first_card_from_deck = player2.put_card_into_playground()
        print_card(player2_first_card_from_deck)

        if player1_first_card_from_deck['value'] > player2_first_card_from_deck['value']:
            player1.take_won_cards_from_play_pile()
            generate_winner_loser_message(player1, player1_first_card_from_deck, player2, player2_first_card_from_deck, MatchType.BATTLE)
        elif player1_first_card_from_deck['value'] < player2_first_card_from_deck['value']:
            generate_winner_loser_message(player2, player2_first_card_from_deck, player1, player1_first_card_from_deck,  MatchType.BATTLE)
        else:
            print(f"\nBoth cards are equal rank. Let's start WAR!")
            break
        
    play_war(player1, player2)
    
def play_war(player1, player2):
    if not check_if_player_has_enough_cards_to_play(player1, player2, 3): return 
    
    while True:
        if not check_if_player_has_enough_cards_to_play(player1, player2, 3): return 
        input(f"{player1.name}, it's your turn to put 4 cards on the table, 3 face down and 1 face up, click enter to put 3 cards face down:")
        player1.put_three_cards_into_playground()
        print_three_empty_cards()
        input(f"{player1.name}, it's your turn, click enter to put 1 card face up:")
        player1_final_card_for_war_from_deck = player1.put_card_into_playground()
        print_card(player1_final_card_for_war_from_deck)     
        
        input(f"{player2.name}, it's your turn put 4 cards on the table, 3 face down and 1 face up, click enter to put 3 cards face down:")
        player2.put_three_cards_into_playground()
        print_three_empty_cards()
        input(f"{player2.name}, it's your turn, click enter to put 1 card face up:")
        player2_final_card_for_war_from_deck = player2.put_card_into_playground()
        print_card(player2_final_card_for_war_from_deck)     
        
        if player1_final_card_for_war_from_deck['value'] > player2_final_card_for_war_from_deck['value']:
            generate_winner_loser_message(player1, player1_final_card_for_war_from_deck, player2, player2_final_card_for_war_from_deck, MatchType.WAR)
            break
        elif player1_final_card_for_war_from_deck['value'] < player2_final_card_for_war_from_deck['value']:
            generate_winner_loser_message(player2, player2_final_card_for_war_from_deck, player1, player1_final_card_for_war_from_deck, MatchType.WAR)
            break
        else:
            print(f"\n Both cards are equal rank. Let's continue WAR!")
    play_battle(player1, player2) 
    
    
    

if __name__=="__main__":
    main()