__author__ = 'Ashly Altman'

# REQUIREMENTS: Create text based Blackjack game
# The game needs to have one player versus automated dealer
# player can stand or hit
# player must be able to pick betting amount
# Alert player of wins, losses, busts, etc

# Blackjack rules:
# Objective: Get as close to 21 as possible without going over
# Card Values: 1-10
# Betting: player begins with $50 and can bet minimum of $2 per round
# Player loses when all money has been lost
# If player reaches $1000 then they get their hands broken by
# casino pit bosses for suspected card counting

# The Deal:
# After player places bet, the dealer gives card to player face up,
# then deals to himself. Then the dealer gives second face up card to player,
# but the dealer's second card is kept face down. Two cards revealed for player
# One hidden card and one revealed card for dealer

# The Play:
# The player goes first and can stand (no card) or hit (receive card)
# After the player decides to stand, the dealer reveals face down card. If
# the dealer's total points are 17 or more, they must stand. If not, they
# take cards until the total is 17 or more.

import random

gameOn = True


class Dealer(object):

    def __init__(self):

        """

        :rtype : object
        """
        self.hand = []
        self.deck = []
        self.current_score = 0

    # generate list of 52 numbers, 1-11, with '10' appearing 16 times, and the rest appearing 4 times.
        for i in range(0, 52):
            if i < 16:
                self.deck.append(10)
            elif 16 <= i <= 48:
                for j in range(1, 10):
                    self.deck.append(j)
            else:
                self.deck[i] = 11

        random.shuffle(self.deck)

    def deal(self):

        return self.deck.pop()

    def score(self, card):

            self.current_score += card


class Player(object):

    def __init__(self):

        self.hand = []
        self.wallet = 50
        self.current_bid = 0
        self.current_score = 0

    def score(self, card):

            self.current_score += card

# PLAY GAME

print("Welcome to BlackJack!")
dealer = Dealer()
player = Player()
bet = 0
playerInput = 0
standOrHit = ''
playAgain = ''

while gameOn:

    print("you have this much money ", player.wallet)
    print("Please place your bet (at least $2!)")
    playerInput = int(input("Amount: $"))


    while bet == 0:
        if 2 <= playerInput < player.wallet:
            bet = playerInput
        elif playerInput > player.wallet:
            playerInput = int(input("A wise guy eh? You aint got that kinda money! Enter Amount: $"))
            bet = playerInput
        else:
            playerInput = int(input("You're mouth is writing checks your ass can't cash! Enter Amount: $"))
            bet = playerInput

    card1 = 0
    card2 = 0
    card1 = dealer.deal()
    card2 = dealer.deal()
    player.hand.append(card1)
    dealer.hand.append(card2)
    player.score(card1)
    dealer.score(card2)

    print("your first card is: ", player.hand[0])
    print("the dealer's first card is: ", dealer.hand[0])

    card1 = 0
    card2 = 0
    card1 = dealer.deal()
    card2 = dealer.deal()
    player.hand.append(card1)
    dealer.hand.append(card2)

    print("your second card is: ", player.hand[1])
    player.score(card1)
    dealer.score(card2)

    while player.current_score < 21:
        print("current score: ", player.current_score)
        standOrHit = input("Stand or Hit? (s/h): ").lower()
        if standOrHit[0] == 'h':

            card1 = dealer.deal()
            player.hand.append(card1)
            player.score(card1)
            continue
        else:
            break

    while dealer.current_score <= 17:

        card2 = dealer.deal()
        dealer.hand.append(card2)
        dealer.score(card2)

    if player.current_score == 21:
        print("Black Jack! You win $", bet*1.5, " ...the gods of fate smile upon thee!")
        player.wallet += bet*1.5
    elif player.current_score > 21:
        print("You busted! You lose: ", bet)
        player.wallet -= bet
    else:
        print("The dealer's score is: ", dealer.current_score)
        if player.current_score > dealer.current_score:
            print("You win $", bet, " ...must be your luck day!")
            player.wallet += bet
        else:
            print("Busted! You lose $", bet, "...can't win em all!")
            player.wallet -= bet

    playAgain = input("play again? y/n")
    if playAgain == 'y':
        player.current_score = 0
        continue
    else:
        break

print("Thanks for playing... chicken!")




























