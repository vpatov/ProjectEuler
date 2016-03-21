"""
 https://projecteuler.net/problem=41
 Pandigital prime


 We shall say that an n -digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime. 
 What is the largest n -digit pandigital prime that exists?
"""

import time
startTime = time.clock()
import itertools
from math import sqrt

def isPrime(n):
    limit = int(sqrt(n)) + 1
    for i in range(2,limit):
        if (n % i == 0):
            return False
    return True



#because 9 + 8 + .. + 1 = 45,
#and 8 + 7 + .. + 1 = 36, thus 9digit and 8digit pandigitals are divisible by 3 and 9, an thus cannot be prime,
# so we start with 7digit pandigitals.

perms = itertools.permutations('7654321')
for perm in perms:
    if isPrime(int(''.join(perm))):
        print(''.join(perm))
        break







endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
