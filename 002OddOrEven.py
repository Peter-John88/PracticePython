#   -*- coding:utf-8  -*-

"""

Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1.If the number is a multiple of 4, print out a different message.
2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

# my solution:

num = int(raw_input("Enter a num:"))
if num % 2 == 0:
    print '%s is even' % num
    if num % 4 == 0:
        print '%s is devided by 4' % num
else:
    print '%s is odd'  % num


print "========================================"

num1 = int(raw_input("Enter num1:"))
check = int(raw_input("Enter check:"))
if check % num1 == 0:
    print '%s is devided by %s' %(check, num1)
else:
    print '%s is not devided by %s' %(check, num1)




# standard solution:

num = input("Enter a number: ")
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")




num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)



