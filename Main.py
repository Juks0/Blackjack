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


def check_if_busted(player):
    return player.countPoints() > 21


def next_move_you(playerYou, croupier):
    card = croupier.takeCard()
    playerYou.hand.append(card)
    translated_card = translate_card(card.value, card.suit)
    if card.suit in [Suit.Hearts, Suit.Diamonds]:
        print(yellow(f"{playerYou.name} received a card: ", 'bold') + red(translated_card))
    else:
        print(yellow(f"{playerYou.name} received a card: ", 'bold') + blue(translated_card))


def check_for_blackjack(player):
    return player.countPoints() == 21


def next_move(players, croupier):
    for player in players:
        player.hand.append(croupier.takeCard())
    print("Players received their cards.")


def translate_card(card_number, suit):
    card_name = card_names.get(card_number, str(card_number))
    return f"{card_name} {suit.value}"


def place_bet(player, tempPlayers=None):
    randomBet = random.randint(1, 4) * 5
    if player.budget >= randomBet:
        player.lastBet = randomBet
        player.budget -= randomBet
        print(f"{player.name} placed a bet of {randomBet}. Remaining budget: {player.budget}")
    else:
        if tempPlayers:
            tempPlayers.remove(player)


def place_bet_you(playerYou, value):
    playerYou.budget -= value
    print(f"{playerYou.name} placed a bet of {value}. Remaining budget: {playerYou.budget}")


def check_did_win(player, croupier):
    if player.countPoints() > croupier.countPoints():
        print(f"{player.name} won!")
        player.budget += player.lastBet * 2
    elif player.countPoints() == croupier.countPoints():
        print(f"{player.name} drew!")
        player.budget += player.lastBet
    else:
        print(f"{player.name} lost!")


def check_for_aces(player):
    return any(card.rank == 'A' for card in player.hand)


if __name__ == "__main__":
    croupier = Croupier()
    players = []
    playerYou = Player()
    print(green("                       Welcome to the game of BlackJack!", 'bold'))

    while True:
        playerCount = int(input("Enter number of players (2-7): "))
        if 2 <= playerCount <= 7:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 7.")

    for _ in range(playerCount - 1):
        players.append(PlayerAi())

    print("Welcome: ")
    for player in players:
        print(f"- {player.name}")
    print("- You")

    budget = int(input("Enter your budget (suggested 50, 100, 150... etc.): "))
    playerYou.budget = budget

    while playerYou.budget > 0:
        playerYou.hand = []
        tempPlayers = players.copy()
        croupier.deck = Deck(include_jokers=False)

        bet = int(input("Enter your bet: "))
        if bet > playerYou.budget:
            print("You don't have enough money to place this bet.")
            continue

        croupier.shuffle()
        place_bet_you(playerYou, bet)

        for player in tempPlayers:
            time.sleep(0.2)
            player.hand = []
            place_bet(player, tempPlayers)

        time.sleep(0.5)
        next_move(tempPlayers, croupier)
        time.sleep(1)
        next_move_you(playerYou, croupier)
        time.sleep(1)
        croupier.takeHisCard()

        if croupier.hand[-1].suit in [Suit.Hearts, Suit.Diamonds]:
            print(f"Croupier received a: " + red(translate_card(croupier.hand[-1].value, croupier.hand[-1].suit)))
        else:
            print(f"Croupier received a: " + blue(translate_card(croupier.hand[-1].value, croupier.hand[-1].suit)))

        next_move(tempPlayers, croupier)
        time.sleep(1)
        next_move_you(playerYou, croupier)
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
            answer = input("Do you want to take another card? (yes/no): ")
            if answer.lower() == 'yes':
                next_move_you(playerYou, croupier)
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
                for card in croupier.hand:
                    print(translate_card(card.value, card.suit), end=", ")
                print()

                while croupier.shouldKeepPlaying():
                    croupier.hand.append(croupier.takeCard())
                croupier.printHand()
                croupierScore = croupier.countPoints()

                if score > 21:
                    print(magenta("You lost!"))
                    playerYou.hand = []
                    break
                else:
                    if croupierScore > 21:
                        print(magenta("Croupier busted! You won!"))
                        playerYou.hand = []
                        playerYou.budget += bet * 2
                        break
                    elif score > croupierScore:
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
            if check_for_blackjack(player):
                print(f"{player.name} has BlackJack!")
                tempPlayers.remove(player)
                player.budget += player.lastBet * 3
            if player.shouldKeepPlaying():
                print(f"{player.name} decided to stay.")
                player.hand.append(croupier.takeCard())
            check_did_win(player, croupier)

        print(blue(f"{playerYou.name}'s budget: {playerYou.budget}", 'underlined'))
        print("")

        if playerYou.budget == 0:
            print("You ran out of money.")
            break

        answer = input("Do you want to play another round? (yes/no): ")
        if answer.lower() == 'no':
            print("Game over.")
            break
