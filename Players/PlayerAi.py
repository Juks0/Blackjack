import random


def generateName():
    playerNames = ['Adam', 'Peter', 'John', 'Paul', 'George', 'Ringo', 'Mick', 'Keith', 'Charlie', 'Brian', 'Bill',
                   'Ronnie', 'Rod', 'Elton', 'Freddie', 'David', 'Roger', 'Robert', 'Jimmy', 'Eric', 'Sting', 'Bono',
                   'Bruce', 'Bob', 'Tom', 'Neil', 'Kurt', 'Eddie', 'Chris', 'Dave', 'Liam', 'Noel', 'Thom', 'Johnny',
                   'Jack', 'Joe', 'Steve', 'Steven', 'Stevie', 'Michael', 'George', 'Phil', 'Nick', 'Tommy', 'Billy',
                   'Joe']
    return playerNames[random.randint(0, len(playerNames) - 1)]


class PlayerAi:

    def __init__(self):
        self.budget = random.randint(0, 20) * 50

        self.name = generateName()
        self.hand = []

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

    def shouldKeepPlaying(self):
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
