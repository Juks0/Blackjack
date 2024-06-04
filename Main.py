"""
The game starts by asking for the number of players, which should be between 2 and 7. One of the players is a human player and the rest are AI players.
Each player is asked to enter their budget. The budget is the amount of money they have to bet in the game.
The game proceeds in rounds. In each round, the human player is asked to place a bet. The bet should be less than or equal to their current budget.
After the human player places their bet, each AI player places a bet. The bet is a random number between 0 and 20, multiplied by 5. If an AI player does not have enough budget to place the bet, they are removed from the game.
Each player, including the human player and the AI players, is dealt a card. The card is taken from the deck by the croupier.
The human player is then asked if they want to take another card. If they choose to take another card, a card is dealt to them. If the total points of their cards exceed 21, they bust and lose their bet.
If the human player chooses not to take another card, their turn ends and their points are compared to the croupier's points. If their points are greater than the croupier's, they win and their budget is increased by twice their bet. If their points are equal to the croupier's, it's a draw and their budget is increased by their bet. If their points are less than the croupier's, they lose and their budget is decreased by their bet.
After the human player's turn, each AI player takes their turn. If an AI player's points are 21, they have a BlackJack and their budget is increased by three times their last bet. If an AI player decides to stay, a card is dealt to them. After an AI player's turn, their points are compared to the croupier's points in the same way as the human player's points.
The game continues in rounds until the human player's budget is 0 or the human player chooses not to play another round.
The game ends when the human player's budget is 0 or the human player chooses not to play another round.
"""


import random
import time

from deck import Suit, Deck
from simple_colors import *
from Players.Player import Player
from Players.PlayerAi import PlayerAi
from Players.Croupier import Croupier

# Mapping of card numbers to their names
card_names = {
    1: 'Ace',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}

def chceckIfBusted(self):
    """
    Checks if the player has busted (i.e., their points exceed 21)

    Returns:
        bool: True if the player has busted, False otherwise
    """
    if self.countPoints() > 21:
        return True
    return False

def nextMoveYou(playerYou, croupier):
    """
    Executes the next move for the human player

    Args:
        playerYou (Player): The human player
        croupier (Croupier): The croupier
    """
    card = croupier.takeCard()
    playerYou.hand.append(card)
    translated_card = translate_card(card.value, card.suit)
    if card.suit in [Suit.Hearts, Suit.Diamonds]:
        print(yellow(playerYou.name + " received a card: ", 'bold') + red(translated_card))
    else:
        print(yellow(playerYou.name + " received a card: ", 'bold') + blue(translated_card))

def checkForBlackJack(self):
    """
    Checks if the player has a BlackJack (i.e., their points equal 21)

    Returns:
        bool: True if the player has a BlackJack, False otherwise
    """
    if self.countPoints() == 21:
        return True
    return False

def nextMove(players, croupier):
    """
    Executes the next move for all players

    Args:
        players (list): List of all players
        croupier (Croupier): The croupier
    """
    for player in players:
        player.hand.append(croupier.takeCard())
    print("Players received their cards.")

def translate_card(card_number, suit):
    """
    Translates a card number and suit into a string representation

    Args:
        card_number (int): The card number
        suit (Suit): The card suit

    Returns:
        str: The string representation of the card
    """
    if card_number in card_names:
        return f"{card_names[card_number]} {suit.value}"
    else:
        return f"{card_number} {suit.value}"

def placeBet(self):
    """
    Places a bet for the player

    The bet is a random number between 0 and 20, multiplied by 5.
    If the player does not have enough budget to place the bet, they are removed from the game.
    """
    randomBet = random.randint(0, 20) * 5
    self.lastBet = randomBet
    tempMoney = self.budget - randomBet
    if tempMoney > 0:
        self.lastBet = randomBet
        self.budget -= randomBet
        print(self.name + " placed a bet of " + str(randomBet) + ". Remaining budget: " + str(self.budget))
    else:
        tempPlayers.remove(self)

def placeBetYou(value):
    """
    Places a bet for the human player

    Args:
        value (int): The bet value
    """
    playerYou.budget -= value
    print(playerYou.name + " placed a bet of " + str(value) + ". Remaining budget: " + str(playerYou.budget))

def checkDidWin(self, croupier):
    """
    Checks if the player has won the game

    If the player's points are greater than the croupier's, they win.
    If the player's points are equal to the croupier's, it's a draw.
    If the player's points are less than the croupier's, they lose.

    Args:
        croupier (Croupier): The croupier
    """
    if self.countPoints() > croupier.countPoints():
        print(self.name + " won!")
        self.budget += self.lastBet * 2
    elif self.countPoints() == croupier.countPoints():
        print(self.name + " drew!")
        self.budget += self.lastBet
    else:
        print(self.name + " lost!")
        self.budget -= self.lastBet

def checkForAces(self):
    """
    Checks if the player has any Aces in their hand

    Returns:
        bool: True if the player has an Ace, False otherwise
    """
    for card in self.hand:
        if card.rank == 'A':
            return True
    return False

# Main game loop
if __name__ == "__main__":
    # Initialization of the game
    croupier = Croupier()
    players = []
    playerYou = Player()
    print(green("                       Welcome to the game of BlackJack!", 'bold'))

    # Game setup: number of players and their budgets
    while True:
        print("Enter number of players(2-7): ")
        playerCount = int(input())
        if 2 <= playerCount <= 7:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 7.")
    for i in range(playerCount - 1):
        players.append(PlayerAi())
    print("Welcome: ")
    for player in players:
        print("- " + player.name)
    print("- " + "You")
    print("Enter your budget(suggested 50,100,150.... etc.): ")
    budget = int(input())
    playerYou.budget = budget

    # Main game loop
    while playerYou.budget > 0:
        # Game round setup
        playerYou.hand = []
        tempPlayers = players.copy()
        croupier.deck = Deck(include_jokers=False)
        print("Enter your bet: ")
        bet = int(input())
        if bet > playerYou.budget:
            print("You don't have enough money to place this bet.")
            continue
        croupier.shuffle()
        placeBetYou(bet)
        for player in tempPlayers:
            time.sleep(0.2)
            player.hand = []
            placeBet(player)
        time.sleep(0.5)
        nextMove(tempPlayers, croupier)
        time.sleep(1)
        nextMoveYou(playerYou, croupier)
        time.sleep(1)
        croupier.takeHisCard()
        if croupier.hand[-1].suit in [Suit.Hearts, Suit.Diamonds]:
            print("Croupier received a: " + red(translate_card(croupier.hand[-1].value, croupier.hand[-1].suit)))
        else:
            print("Croupier received a: " + blue(translate_card(croupier.hand[-1].value, croupier.hand[-1].suit)))
        nextMove(tempPlayers, croupier)
        time.sleep(1)
        nextMoveYou(playerYou, croupier)
        time.sleep(1)
        croupier.takeHisCard()
        print("\n")

        # Player's turn
        while playerYou.countPoints() <= 21:
            playerYou.printHand()
            if playerYou.countPoints() == 21:
                print(magenta("You have BlackJack!", 'bold'))
                playerYou.hand = []
                playerYou.budget += bet * 3
                break
            print("Do you want to take another card? (yes/no)")
            answer = input()
            if answer == 'yes':
                nextMoveYou(playerYou, croupier)
                if playerYou.countPoints() > 21:
                    print(magenta("You busted!"))
                    playerYou.hand = []
                    break
            else:
                print("You decided to stay.")
                playerYou.printHand()
                score = playerYou.countPoints()

                # Croupier's turn
                print("Croupier's turn.")
                print("Croupier's hand: ", end="")
                for index, card in enumerate(croupier.hand):
                    print(translate_card(card.value, card.suit), end=", ")
                print()
                while croupier.shouldKeepPlaying():
                    croupier.hand.append(croupier.takeCard())
                croupier.printHand()
                croupierScore = croupier.countPoints()
                if score > 21:
                    print(magenta("You lost!"))
                    playerYou.hand= []
                    break
                else:
                    if croupierScore > 21:
                        print(magenta("Croopier busted!, You won!"))
                        playerYou.hand = []
                        playerYou.budget += bet * 2
                        break
                    if score > croupierScore:
                        print(magenta("You won!"))
                        playerYou.hand = []
                        playerYou.budget += bet * 2
                        break
                    elif score == croupierScore:
                        print(magenta("It's a draw!"))
                        playerYou.hand = []
                        playerYou.budget += bet
                        break
                    else:
                        print(magenta("You lost!"))
                        playerYou.hand = []
                        break
        print("")
        time.sleep(0.5)

        # Other players' turns
        for player in tempPlayers:
            if player.countPoints() == 21:
                print(player.name + " has BlackJack!")
                tempPlayers.remove(player)
                player.budget += player.lastBet * 3
            if player.shouldKeepPlaying():
                print(player.name + " decided to stay.")
                player.hand.append(croupier.takeCard())
            checkDidWin(player, croupier)
        print(blue(playerYou.name + "r's budget: " + str(playerYou.budget), 'underlined'))
        print("")

        # End of game round
        if playerYou.budget == 0:
            print("You ran out of money.")
            break
        print("Do you want to play another round? (yes/no)")
        answer = input()
        if answer == 'no':
            print("Game over.")
            break