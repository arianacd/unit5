# by Ariana Daney
# last modified October 21, 2019
# this program allows a user to guess a random number that the computer has


import random


def main():
    while True:
        user_answer = input("do you want to play a guessing game?, if yes, enter y and if no, enter n")
        if user_answer == "y" or user_answer == "n":
            break
    if user_answer == "y":
        print("awesome!, lets play")
    else:
        for x in range(300):
            print("terminating")
    computer_num = random.randint(1, 100)
    user_guess = input(int("what do you think the computers' number is"))


main()
