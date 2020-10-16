
from card import Card

class Hand():

    def __init__(self):

        self.cards = []
        self.value = 0
        self.ace_count = 0

    def add_card(self, card):

        self.cards.append(card)

        if card.rank == 'Ace':
            self.ace_count += 1
        
        self.calculate_value()

    def calculate_value(self):

        value = 0

        for card in self.cards:
            
            if card.rank != 'Ace':
                value += card.value

        for _ in range(self.ace_count):

            if value + 11 < 21:
                value += 11
            else:
                value += 1
        
        self.value = value



    def __str__(self):

        message_array = ["\nYou have the following cards: \n"]

        for card in self.cards:
            message_array.append('\t' + str(card) + '\n')

        message_array.append(f"You hand's value is {self.value}\n")

        return ''.join(message_array)