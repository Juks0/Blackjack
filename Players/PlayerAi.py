import random

def generateName():
    """
    Generates a random name for the AI player from a predefined list of names.

    Returns:
        str: The generated name.
    """
    playerNames = ['Adam', 'Peter', 'John', 'Paul', 'George', 'Ringo', 'Mick', 'Keith', 'Charlie', 'Brian', 'Bill',
                   'Ronnie', 'Rod', 'Elton', 'Freddie', 'David', 'Roger', 'Robert', 'Jimmy', 'Eric', 'Sting', 'Bono',
                   'Bruce', 'Bob', 'Tom', 'Neil', 'Kurt', 'Eddie', 'Chris', 'Dave', 'Liam', 'Noel', 'Thom', 'Johnny',
                   'Jack', 'Joe', 'Steve', 'Steven', 'Stevie', 'Michael', 'George', 'Phil', 'Nick', 'Tommy', 'Billy',
                   'Joe']
    return playerNames[random.randint(0, len(playerNames) - 1)]


class PlayerAi:
    """
    Represents an AI player in a game of BlackJack.

    Attributes:
        lastBet (int): The last bet placed by the AI player.
        budget (int): The AI player's budget for betting.
        name (str): The name of the AI player.
        hand (list): The cards in the AI player's hand.
    """

    def __init__(self):
        """
        Initializes a new instance of the PlayerAi class.
        """
        self.lastBet = None
        self.budget = random.randint(5, 20) * 50
        self.name = generateName()
        self.hand = []

    def countPoints(self):
        """
        Counts the points in the AI player's hand.

        Returns:
            int: The total points in the AI player's hand.
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

    def shouldKeepPlaying(self):
        """
        Determines whether the AI player should keep playing based on their current points and the number of cards in their hand.

        Returns:
            bool: True if the AI player should keep playing, False otherwise.
        """
        points = self.countPoints()
        if len(self.hand) == 1:
            return points < 17
        if len(self.hand) == 2:
            return points < 14
        if len(self.hand) == 3:
            return points < 13
        if len(self.hand) == 4:
            return points < 12
        return False