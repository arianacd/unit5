# by Ariana Daney
# last modified October 21, 2019
# this program allows a user to guess a random number that the computer has


import random


def main():
    # this while True loop makes it possible to play the game multiple times
    while True:
        # this while True loop asks the user if they want to play the game and then answers
        while True:
            user_answer = input("do you want to play a guessing game?, if yes, enter y and if no, enter n")
            if user_answer == "y" or user_answer == "n":
                break
        if user_answer == "y":
            print("awesome!, lets play")
        else:
            print("thanks for the the consideration")
            break
        computer_num = random.randint(1, 100)
        tries = 0
        # this while True loop allows the user to guess a number and then tells them if their number is too high or low
        # this while True loop also tells the user the amount of tries it takes the user to guess the computers number
        while True:
            user_guess = int(input("what do you think the computers' number is"))
            tries += 1
            if user_guess == computer_num:
                print("you guessed correctly! congrats!")
                break
            elif user_guess < 1 or user_guess > 100:
                print("your number is not in the correct range of 1 to 100, guess again")
            elif user_guess > computer_num:
                print("your guess was too high, try again!")
            else:
                print("your guess was too low, try again!")
        print("it took you", tries, "tries to guess the computers number!")


main()
