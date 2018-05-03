#  -*-  coding:utf-8   -*-

"""

Exercise 1

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1.Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2.Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""

# my solutions:

name = input("Enter your name:")
age = input("Enter your age:")
s = "Hi, %s ! There are %s years thar you will turn 100 years old!\n"  %(name, 100-int(age))
print s

# standard solutions:

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)

# knowledge summary:
  # https://github.com/Peter-John88/ConquerPython/blob/master/005raw_input%20and%20input

