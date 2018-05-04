# -*- coding:utf-8  -*-

"""

Exercise 8

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

- Rock beats scissors
- Scissors beats paper
- Paper beats rock

"""


# my solution

def user_input_compare():
    user1_input = raw_input("user1 Enter your guess (Rock|Scissors|Paper):")
    user2_input = raw_input("user2 Enter your guess (Rock|Scissors|Paper):")

    if user1_input == "Rock":
        if user2_input == "Rock":
            print "Tied"
        if user2_input == "Scissors":
            print "User1 Win!"
        if user2_input == "Paper":
            print "User2 Win!"
    elif user1_input == "Scissors":
        if user2_input == "Rock":
            print "User2 Win!"
        if user2_input == "Scissors":
            print "Tied"
        if user2_input == "Paper":
            print "User1 Win!"
    elif user1_input == "Paper":
        if user2_input == "Rock":
            print "User1 Win!"
        if user2_input == "Scissors":
            print "User2 Win!"
        if user2_input == "Paper":
            print "Tied"

while True:
    is_continue = raw_input("Guess once again?  (Y|N)  :")
    if is_continue == 'Y':
        user_input_compare()
    elif is_continue == 'N':
        break


# standard solution 1

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))





# standard solution 2

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')

