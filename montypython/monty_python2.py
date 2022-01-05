#!/usr/bin/env python3
"""
Conditionals - Life of Brian guessing game using a while loop.
"""

def main():
    # using counter to track rounds
    round = 0
    
    reply = ["Correct!", "Sorry, try again!\n", "Sorry, the answer is Brian."]

    while round < 3:
        # incriment the round
        round += 1

        print("Finish the movie title, \"Monty Python's The Life of ...\"")
        response = input("Your guess --> ")

        if response == "Brian":
            print(reply[0])
            break
        elif round == 3:
            print(reply[2])
        else:
            print(reply[1])

main()
