# -*-  coding:utf-8  -*-

"""

Exercise 11

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

"""

# my solution

def is_prime(num):
    """if num have divisor, then num is not a prime """

    divisors = []

    if num == 1:
        print "%s is not a prime!" % num
    elif num == 2:
        print "%s is a prime!" % num
    else:
        for i in range(2, num):
            if num % i == 0:
                divisors.append(i)

        if len(divisors)==0:
            print "%s is a prime!" % num
        else:
            print "%s is not a prime!" % num

num = int(raw_input("Enter a num:"))
is_prime(num)



# standard solution

num = int(raw_input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(num):
    if num > 1:
        if len(a) == 0:
            print 'prime'
        else:
            print 'NOT prime'
    else:
        print 'NOT prime'

is_prime(num)





