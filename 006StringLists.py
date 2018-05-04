# -*-  coding:utf-8  -*-

"""

Exercise 6

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

"""

# my solution:
string1 = raw_input("Enter a string:")
l1 = len(string1)
L=[]
for i in range(-1,-(l1+1),-1):
    L.append(string1[i])
string2 = ''.join(L)

if string1 == string2:
    print 'string1 is a palindrome!'
else:
    print 'string1 is not a palindrome!'



# standard solution:

 #A sample solution using string reversal
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

 #A sample solution using for loops
def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
        return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')



