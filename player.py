from hand import Hand
from card import Card

class Player():

    def __init__(self, chips):

        self.chips = chips
        self.hand = Hand()

    def add_card(self, card):
        self.hand.add_card(card)

    def remove_chips(self, amount):

        if amount <= self.chips:
            self.chips -= amount
            print(f'Player has bet {amount} chips.')
        else:
            print("Player doesn't have enough chips!") 
    
    def add_chips(self, amount):
        self.chips += amount
        print(f'Player has won {amount} chips.')
    
    def __str__(self):
        return f"Player's Hand: {self.hand.value}, Player's Chips: {self.chips}"
