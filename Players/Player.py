from deck import Suit
from simple_colors import *

class Player:
    """
    Represents a player in a game of BlackJack.

    Attributes:
        budget (int): The player's budget for betting.
        name (str): The name of the player.
        hand (list): The cards in the player's hand.
    """

    def __init__(self):
        """
        Initializes a new instance of the Player class.
        """
        self.budget = 0
        self.name = "You"
        self.hand = []

    def takeCard(self, card):
        """
        Adds a card to the player's hand.

        Args:
            card (Card): The card to add to the hand.
        """
        self.hand.append(card)

    def showHand(self):
        """
        Returns the player's hand.

        Returns:
            list: The player's hand.
        """
        return self.hand

    def discard(self, card):
        """
        Removes a card from the player's hand.

        Args:
            card (Card): The card to remove from the hand.
        """
        self.hand.remove(card)

    def discardHand(self):
        """
        Discards the player's hand.
        """
        self.hand = []

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
        if card_number in card_names:
            card_name = card_names[card_number]
        else:
            card_name = str(card_number)

        if suit in [Suit.Hearts, Suit.Diamonds]:
            return red(f"{card_name} {suit.value}")
        else:
            return blue(f"{card_name} {suit.value}")

    def printHand(self):
        """
        Prints the player's hand.
        """
        print(self.name + "'s hand: ", end="")
        for index, card in enumerate(self.hand):
            print(self.translate_card(card.value, card.suit), end=", ")
        print()

    def countPoints(self):
        """
        Counts the points in the player's hand.

        Returns:
            int: The total points in the player's hand.
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

    def __str__(self):
        """
        Returns a string representation of the player.

        Returns:
            str: The name of the player.
        """
        return self.name

    def __repr__(self):
        """
        Returns a string representation of the player.

        Returns:
            str: The name of the player.
        """
        return self.name