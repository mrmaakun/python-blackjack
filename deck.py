
from card import Card
from random import shuffle

suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck():

    def __init__(self):
        self.cards = []

        # Add all cards to deck
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

        self.shuffle_deck()        

    def shuffle_deck(self):
        shuffle(self.cards)


    def deal_card(self):

        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No more cards")
            return None

    def __str__(self):
        return f"Deck has {len(self.cards)} cards left."


