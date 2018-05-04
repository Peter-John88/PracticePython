# -*-  coding:utf-8  -*-

"""

Exercise 7

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

"""


# my solution:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print [i for i in a if i % 2 == 0]


# standard solution:

    #And for a “complete” solution, look at this:
__author__ = 'jhunt'

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]

print(b)

    #For a solution that uses the random library to generate test lists, check this out:
import random

numlist = []
list_length = random.randint(5,15)


while len(numlist) < list_length:
    numlist.append(random.randint(1,75))


evenlist = [number for number in numlist if number % 2 == 0]

print(numlist)
print(evenlist)
