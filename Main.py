import random
import time

from deck import Suit, Deck
from simple_colors import *
from Players.Player import Player
from Players.PlayerAi import PlayerAi
from Players.Croupier import Croupier

card_names = {
    1: 'Ace',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}


def chceckIfBusted(self):
    if self.countPoints() > 21:
        return True
    return False


def nextMoveYou(playerYou, croupier):
    card = croupier.takeCard()
    playerYou.hand.append(card)
    translated_card = translate_card(card.value, card.suit)
    if card.suit in [Suit.Hearts, Suit.Diamonds]:
        print(yellow(playerYou.name + " received a card: ", 'bold') + red(translated_card))
    else:
        print(yellow(playerYou.name + " received a card: ", 'bold') + blue(translated_card))


def checkForBlackJack(self):
    if self.countPoints() == 21:
        return True
    return False


def nextMove(players, croupier):
    for player in players:
        player.hand.append(croupier.takeCard())
    print("Players received their cards.")


def translate_card(card_number, suit):
    if card_number in card_names:
        return f"{card_names[card_number]} {suit.value}"
    else:
        return f"{card_number} {suit.value}"


def placeBet(self):
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
    playerYou.budget -= value
    print(playerYou.name + " placed a bet of " + str(value) + ". Remaining budget: " + str(playerYou.budget))




def checkDidWin(self, croupier):
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
    for card in self.hand:
        if card.rank == 'A':
            return True
    return False


if __name__ == "__main__":
    croupier = Croupier()
    players = []
    playerYou = Player()
    print(green("                       Welcome to the game of BlackJack!", 'bold'))
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
    while playerYou.budget > 0:
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
        if playerYou.budget == 0:
            print("You ran out of money.")
            break
        print("Do you want to play another round? (yes/no)")
        answer = input()
        if answer == 'no':
            print("Game over.")
            break



