import math 
import random
from sty import fg, rs
import sys

a = []
a.append(random.randint(1, 99))

print(fg(0, 255, 0) + "Hello my Friend, Welcome to Guess The Number game!\n" + fg.rs)

temp = None
zen = None
guess = 0

def play_again(x):
    if x == "y" or x == "yes" or x == "Yes" or x == "YES":
        return True
    elif x == "n" or x == "no" or x == "No" or x == "NO":
        return False

while True:
    if temp == True:
        while zen != True:
            again = input(fg(255,105,180) + "Would you like to play again? " + fg.rs)
            if again == 'quit':
                sys.exit()
            if play_again(again) == False:
                print(fg(255,215,0) + "Good-bye! See you soon!" + fg.rs)
                zen = False
                sys.exit()
            elif play_again(again) == True:
                a.clear()
                a.append(random.randint(1, 99))
                zen = True
            else:
                print(fg(255, 10, 10) + "Give yes or no!" + fg.rs)
            temp = False
        zen = None
    guess += 1
    ask = input("Try to guess the number between 1 and 99: ")
    if ask == "quit":
        print(fg(255,215,0) + "Good-bye! See you soon!" + fg.rs)
        sys.exit()
    if ask.isdigit()and int(ask) > 0 and int(ask) <= 99:
        n = int(ask)
        for i in range(len(a)):
            if n < a[i]:
                print(fg(255,127,80) + "Guess is low" + fg.rs)
            elif n > a[i]:
                print(fg(255,127,80) + "Guess is high" + fg.rs)
            elif n == a[i]:
                print(fg(10, 255, 10) + "You guessed it in "+ str(guess) + " rounds!" + fg.rs)
                guess = 0
                temp = True
    else:
        if ask != "quit":
            print(fg(255, 10, 10) + "You must give a number between 1 and 99!" + fg.rs)
            