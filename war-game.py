import random

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        
    def __str__(self):
        return f"Name: {self.name}, cards: {self.cards}"
        
def generate_two_shuffled_decks():
    card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    random.shuffle(card_deck)
    return card_deck
    
def split_list(lst):
    mid = len(lst) // 2  # Find the middle index
    return lst[:mid], lst[mid:]  # Split into two halves




def main():
    half_deck_1, half_deck_2 = split_list(generate_two_shuffled_decks())

    player1 = Player("Player1", half_deck_1)
    player2 = Player("Player2", half_deck_2)
    print(player1)
    print(player2)
    player1_first_card_from_deck = player1.cards.pop(0)
    player2_first_card_from_deck = player2.cards.pop(0)
    figure_out_who_wons_the_battle(player1_first_card_from_deck, player2_first_card_from_deck, player1, player2)

    

    
def figure_out_who_wons_the_battle(player1_first_card_from_deck, player2_first_card_from_deck, player1, player2):
    if player1_first_card_from_deck > player2_first_card_from_deck:
        player1.cards.append(player1_first_card_from_deck)
        player1.cards.append(player2_first_card_from_deck)
        print("Player 1 won, current deck: ", player1.cards)
        print("Player 2 lost, current deck: ", player2.cards)
        return 
    

    
    

if __name__=="__main__":
    main()