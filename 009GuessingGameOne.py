#  -*- coding:utf-8  -*-

"""

Exercise 9

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

1.Keep the game going until the user types “exit”
2.Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

# my solution:

import random
random.seed(5)
answer_num = random.randint(1,9)
print answer_num

guess_history = []

while True:
    is_exit = raw_input("Exit the guess game? (enter 'exit' if exit, otherwise enter anything.) :")
    if is_exit == "exit":
        print "the num you have guessed are: %s" % guess_history
        break
    else:
        user_guess = int(raw_input("Enter your guess num:"))
        guess_history.append(user_guess)
        if user_guess == answer_num:
            print "Exactly right! And the num you have guessed are: %s" % guess_history
        elif user_guess < answer_num:
            print "Too low! And the num you have guessed are: %s" % guess_history
        else:
            print "Too high! the num you have guessed are: %s" % guess_history


# standard answer:

import random

number = random.randint(1,9)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess?")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")
