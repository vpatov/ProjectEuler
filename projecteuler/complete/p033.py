"""
 https://projecteuler.net/problem=33
 Digit cancelling fractions

 The fraction 49 / 98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49 / 98 = 4 / 8 , which is correct, is obtained by cancelling the 9s. 
 We shall consider fractions like, 30 / 50 = 3 / 5 , to be trivial examples. 
 There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator. 
 If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import time
from fractions import Fraction
startTime = time.perf_counter()

def digitCancelling(i,j):
    m = set(str(i))
    n = set(str(j))
    inter = m.intersection(n)
    if len(inter) == 0:
        return False
    else :
        m -= inter
        n -= inter
        if (len(m) == 0 or len(n) == 0):
            return False

        if (Fraction(int(n.pop()),int(m.pop()))) == Fraction(j,i):
            return True
        else: return False

print(digitCancelling(98,49))


nonTrivialSet = set()
for i in range(10,99):
    for j in range(10,99):
        if (i < j):
            break

        if (i % 10 == 0 or j % 10 == 0):
            continue

        if (digitCancelling(i,j)):
            nonTrivialSet.add(Fraction(j,i))

prod = 1
for frac in nonTrivialSet:
    prod *= frac

print(prod.denominator)



endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
