import math 
import random
from sty import fg, rs
import sys

a = []
a.append(random.randint(1, 99))

print(fg(0, 255, 0) + "Hello my Friend, Welcome to my Guess The Number game!\n" + fg.rs)

temp = None

while True:
    print(a)
    if temp == True:
        again = input(fg(255,105,180) + "Would you like to play again? " + fg.rs)
        if again == "n" or again == "no" or again == "No" or again == "N" or again == "NO":
            print(fg(255,215,0) + "Good-bye! See you soon!" + fg.rs)
            sys.exit()
        elif again == "y" or again == "yes" or again == "Yes" or again == "Y" or again == "YES":
            a.clear()
            a.append(random.randint(1, 99))
        else:
            print(fg(255, 10, 10) + "Give a valid value you retard bastard!" + fg.rs)
            sys.exit()
        temp = False
    ask = input("Try to guess the number between 1 and 99: ")
    if ask == "quit":
        print(fg(255,215,0) + "Good-bye! See you soon!" + fg.rs)
        sys.exit()
    if ask.isdigit()and int(ask) > 0 and int(ask) <= 99:
        n = int(ask)
        for i in range(len(a)):
            if n < a[i]:
                print(fg(255,127,80) + "guess is low" + fg.rs)
            elif n > a[i]:
                print(fg(255,127,80) + "guess is high" + fg.rs)
            elif n == a[i]:
                print(fg(10, 255, 10) + "you guessed it!" + fg.rs)
                temp = True
    else:
        if ask != "quit":
            print(fg(255, 10, 10) + "You must give a number between 1 and 99!" + fg.rs)
            