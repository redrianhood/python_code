#!/usr/bin/env python3
"""
Conditionals - Life of Brian guessing game using a better while loop.
"""

def main():
    # using counter to track rounds
    round = 0
    # track response for logic
    response = " "
    # possible replies    
    reply = ["Correct!", "Sorry, try again!\n", "Sorry, the answer is Brian."]


    while round < 3 and response != "Brian":
        round += 1      # incriment the round
        response = input("Finish the movie title, \"Monty Python's The Life of _______\": ")

        if response == "Brian":
            print(reply[0])
        elif round == 3:
            print(reply[2])
        else:
            print(reply[1])

main()
