import math
import random
from sty import fg, rs
import sys


def exitGame():
    print(fg(255,215,0) + "Good-bye! See you soon!" + fg.rs)
    sys.exit()


def getGuess():
    """This function asks the user to guess an number, and continues looping 
    until a valid answer is given.  Must be an integer between 1 and 99.
    """
    # Error checking for non-integer numbers
    try:
        ask = input("Try to guess the number between 1 and 99: ")
        if ask == "quit":
            exitGame()
        ask = int(ask)

    # If answer isn't an integer, repeat function to ask again
    except ValueError:
        print(fg(255, 10, 10) + "You must give a number between 1 and 99!\n" + fg.rs)
        ask = getGuess()
        return ask
    
    # If answer is an integer, and in the correct range then continue.
    if ask > 0 and ask < 100:
        return ask
    
    # If answer is outside of range, repeat function to ask again
    else:
        print(fg(255, 10, 10) + "You must give a number between 1 and 99!\n" + fg.rs)
        ask = getGuess()
        return ask


def repeatGame():
    again = input(fg(255,105,180) + "Would you like to play again? " + fg.rs)
    if again.lower() in ['n', 'no']:
        exitGame()

    # If the player wants to play again, start the main function again
    elif again.lower() in ["y", "yes"]:
        main()

    # If the player doesn't enter a valid choice, repeat the function
    else:
        print(fg(255, 10, 10) + "Give a valid value!\n" + fg.rs)
        repeatGame()


def checkGuess(n, a):
    if n < a:
        print(fg(255,127,80) + "guess is low\n" + fg.rs)

    elif n > a:
        print(fg(255,127,80) + "guess is high\n" + fg.rs)

    elif n == a:
        print(fg(10, 255, 10) + "you guessed it!" + fg.rs)
        repeatGame()


def main():
    # Set the random number for user to guess
    a = random.randint(1, 99)
    
    # Simple loop to ask for a number and then check it
    while True:
        n = getGuess()
        checkGuess(n, a)


if __name__ == "__main__":
    print(fg(0, 255, 0) + "Hello my Friend, Welcome to my Guess The Number game!\n" + fg.rs)
    main()
