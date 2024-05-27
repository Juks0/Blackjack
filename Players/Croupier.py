import random
from deck import Suit, Deck
from simple_colors import *

def generateName():
    playerNames = ['Adam', 'Peter', 'John', 'Paul', 'George', 'Ringo', 'Mick', 'Keith', 'Charlie', 'Brian', 'Bill',
                   'Ronnie', 'Rod', 'Elton', 'Freddie', 'David', 'Roger', 'Robert', 'Jimmy', 'Eric', 'Sting', 'Bono',
                   'Bruce', 'Bob', 'Tom', 'Neil', 'Kurt', 'Eddie', 'Chris', 'Dave', 'Liam', 'Noel', 'Thom', 'Johnny',
                   'Jack', 'Joe', 'Steve', 'Steven', 'Stevie', 'Michael', 'George', 'Phil', 'Nick', 'Tommy', 'Billy',
                   'Joe']
    return playerNames[random.randint(0, len(playerNames) - 1)]

class Croupier:
    limit = 21

    def translate_card(self, card_number, suit):
        card_names = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        card_name = card_names.get(card_number, str(card_number))
        if suit in [Suit.Hearts, Suit.Diamonds]:
            return red(f"{card_name} {suit.value}")
        else:
            return blue(f"{card_name} {suit.value}")

    def __init__(self):
        self.name = generateName()
        self.deck = Deck(include_jokers=False)
        self.hand = []

    def showHand(self):
        return self.hand

    def discardHand(self):
        self.hand = []

    def shuffle(self):
        self.deck.shuffle()
        print("Deck shuffled.")

    def takeCard(self):
        return self.deck.pop()

    def takeHisCard(self):
        self.hand.append(self.deck.pop())

    def shouldKeepPlaying(self):
        points = self.countPoints()
        return points < 17

    def printHand(self):
        print("Croupier's hand: ", end="")
        for card in self.hand:
            print(self.translate_card(card.value, card.suit), end=", ")
        print()

    def countPoints(self):
        points = 0
        aces = 0
        for card in self.hand:
            if card.value in [11, 12, 13]:
                points += 10
            elif card.value == 1:
                points += 11
                aces += 1
            else:
                points += card.value
        while points > 21 and aces:
            points -= 10
            aces -= 1
        return points
