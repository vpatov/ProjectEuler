"""
 https://projecteuler.net/problem=36
 Double-base palindromes


 The decimal number, 585 = 1001001001 2 (binary), is palindromic in both bases. 
 Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2. 
 (Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import time
startTime = time.clock()

"{0:b}".format(10)

def palindromic(num):
    dec = str(num)
    bin = "{0:b}".format(num)
    return dec == dec[::-1] and bin == bin[::-1]

#it almost looks like i wrote no code!!!
print(sum(filter(palindromic,range(1,1000000))))



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
