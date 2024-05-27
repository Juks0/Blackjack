from deck import Suit
from simple_colors import *

class Player:
    def __init__(self):
        self.budget = 0
        self.name = "You"
        self.hand = []

    def takeCard(self, card):
        self.hand.append(card)

    def showHand(self):
        return self.hand

    def discard(self, card):
        self.hand.remove(card)

    def discardHand(self):
        self.hand = []

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

    def printHand(self):
        print(f"{self.name}'s hand: ", end="")
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
