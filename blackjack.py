
from card import Card
from deck import Deck
from hand import Hand
from player import Player


def take_bet(player):

    bet = ''
    digit_check = False

    print (f"You have {player.chips} chips.")

    digit_check = False
    amount_check = False

    while digit_check == False or amount_check == False:

        bet = input("How much would you like to bet? ")

        if bet.isdigit() == False:
            print("Please enter a number.")
            continue
        else:
            digit_check = True
        
        if int(bet) > player.chips:
            print (f"You only have {player.chips} chips. Please bet less than what you have.")
        else:
            amount_check = True
            
    
    player.chips -= int(bet)
    print (f"You now have {player.chips} chips left.")

    return int(bet)

def deal_hand(hand, deck):

    for _ in range(2):
        hand.add_card(deck.deal_card())

def print_dealer_hand(dealer_hand):
    print('The dealer has: ')
    for card in dealer_hand.cards:
        print(f'\t {card}')
        
    print(f"The dealer hand's value is {dealer_hand.value}\n")


if __name__ == '__main__':

    player = Player(1000)

    game_on = True

    while game_on:

        round_bet = take_bet(player)

        # Reset deck and hands
        deck = Deck()
        dealer_hand = Hand()
        player.hand = Hand()

        deal_hand(dealer_hand, deck)
        deal_hand(player.hand, deck)

        print(f"\nDealer has a {dealer_hand.cards[0]}")
        print(player.hand)

        hit = True
        while hit == True:
            input_valid = False

            hit_choice = input ("Would you like another card? ('Y/N') ")

            while input_valid == False:

                if hit_choice.upper() == 'Y':
                    input_valid = True
                    player.add_card(deck.deal_card())
                    print(player.hand)

                    if player.hand.value > 21:
                        hit = False

                elif hit_choice.upper() == 'N':
                    input_valid = True
                    print (f"You've chosen to stay at {player.hand.value}")
                    hit = False
                else:
                    print ("Please pick 'Y' or 'N")
                    
        while dealer_hand.value < player.hand.value:
            dealer_hand.add_card(deck.deal_card())

        #decide winner

        if player.hand.value <= 21:
            print_dealer_hand(dealer_hand)
            if dealer_hand.value > 21:
                print(f"The dealer has busted! You won {round_bet*2} chips!")
                player.chips += round_bet*2
            elif player.hand.value < dealer_hand.value:
                print(f"The dealer wins! You lose the {round_bet} chips you bet.")
            elif player.hand.value > dealer_hand.value:
                print(f"You win! You won {round_bet*2} chips!")
                player.chips += round_bet*2
            else:
                print('You have tied with the dealer. You get your chips back.')
                player.chips += round_bet
        else:
            print("You have busted. The dealer wins!")

        
        #Check if player is out of chips

        if player.chips <= 0:
            print("You are out of chips! GAME OVER!")
            print("See you next time!")
            game_on = False
            break

        input_valid = False
        while input_valid == False:
            choice = input("Would you like to play again? ")
            
            if choice.upper() == 'Y':
                print("Awesome! Let's play again!")
                input_valid = True
            elif choice.upper() == 'N':
                print("Okay, thanks for playing!")
                input_valid = True
                game_on = False
            else:
                print("Please enter 'Y' or 'N'")
                continue

