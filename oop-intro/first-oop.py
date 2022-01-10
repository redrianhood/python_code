#!/usr/bin/env python3
"""
A simple dice program utilizing classes
"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []  # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1, 6))  # 1-6 inclusive

    # unnecessary, see below implementation
    def get_dice(self):  # returns the dice rolls
        return self.dice


def main():
    """ called at runtime """

    # create player objects
    player1 = Player()
    player2 = Player()

    player1.roll()
    player2.roll()

    # determine the winner
    # REEXAMINE, player.dice?
    print("what is player1.dice?: ", player1.dice)
    print("what is player2.dice?: ", player2.dice)
    if sum(player1.dice) == sum(player2.dice):
        print("Draw!")
    elif sum(player1.dice) > sum(player2.dice):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == "__main__":
    main()

