"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time
startTime = time.clock()

#highest product of two 3-digit numbers is 999*999 = 998001

def isPalindrome(n):
    string = str(n)
    return string == string[::-1]

i = 999
j = 999
found = False
bound = 800
while (not found):
    while (i >= bound and not found):
        while (j >= bound and not found):
            if (isPalindrome(i*j)):
                print(i*j)
                found = True
            j -=1
        i -=1
        j = 999
    i = bound
    j = bound
    bound -= 100

endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
