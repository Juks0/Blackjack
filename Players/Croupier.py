import random
from deck import Suit, Deck
from simple_colors import *

def generateName():
    """
    Generates a random name for the croupier from a predefined list of names.

    Returns:
        str: The generated name.
    """
    playerNames = ['Adam', 'Peter', 'John', 'Paul', 'George', 'Ringo', 'Mick', 'Keith', 'Charlie', 'Brian', 'Bill',
                   'Ronnie', 'Rod', 'Elton', 'Freddie', 'David', 'Roger', 'Robert', 'Jimmy', 'Eric', 'Sting', 'Bono',
                   'Bruce', 'Bob', 'Tom', 'Neil', 'Kurt', 'Eddie', 'Chris', 'Dave', 'Liam', 'Noel', 'Thom', 'Johnny',
                   'Jack', 'Joe', 'Steve', 'Steven', 'Stevie', 'Michael', 'George', 'Phil', 'Nick', 'Tommy', 'Billy',
                   'Joe']
    return playerNames[random.randint(0, len(playerNames) - 1)]

class Croupier:
    """
    Represents the croupier in a game of BlackJack.

    Attributes:
        limit (int): The maximum points a player can have without busting.
        name (str): The name of the croupier.
        deck (Deck): The deck of cards the croupier uses.
        hand (list): The cards in the croupier's hand.
    """
    limit = 21

    def translate_card(self, card_number, suit):
        """
        Translates a card number and suit into a string representation.

        Args:
            card_number (int): The card number.
            suit (Suit): The card suit.

        Returns:
            str: The string representation of the card.
        """
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
        """
        Initializes a new instance of the Croupier class.
        """
        self.name = generateName()
        self.deck = Deck(include_jokers=False)
        self.hand = []

    def showHand(self):
        """
        Returns the croupier's hand.

        Returns:
            list: The croupier's hand.
        """
        return self.hand

    def discardHand(self):
        """
        Discards the croupier's hand.
        """
        self.hand = []

    def shuffle(self):
        """
        Shuffles the croupier's deck.
        """
        self.deck.shuffle()
        print("Deck shuffled.")

    def takeCard(self):
        """
        Takes a card from the croupier's deck.

        Returns:
            Card: The card taken from the deck.
        """
        return self.deck.pop()

    def takeHisCard(self):
        """
        Takes a card from the croupier's deck and adds it to his hand.
        """
        self.hand.append(self.deck.pop())

    def shouldKeepPlaying(self):
        """
        Determines whether the croupier should keep playing based on his current points.

        Returns:
            bool: True if the croupier should keep playing, False otherwise.
        """
        points = self.countPoints()
        return points < 17

    def printHand(self):
        """
        Prints the croupier's hand.
        """
        print("Croupier's hand: ", end="")
        for card in self.hand:
            print(self.translate_card(card.value, card.suit), end=", ")
        print()

    def countPoints(self):
        """
        Counts the points in the croupier's hand.

        Returns:
            int: The total points in the croupier's hand.
        """
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