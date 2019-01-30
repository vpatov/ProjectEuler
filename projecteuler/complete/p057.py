"""
 https://projecteuler.net/problem=57
 Square root convergents

 It is possible to show that the square root of two can be expressed as an infinite continued fraction. 
sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
 By expanding this for the first four iterations, we get: 
 1 + 1/2 = 3/2 = 1.5 
1 + 1/(2 + 1/2) = 7/5 = 1.4 
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666... 
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379... 
 The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
 is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

 In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

import time
startTime = time.perf_counter()
from fractions import Fraction
import sys
sys.setrecursionlimit(1100)

count = 0



"""
1 + 1/2
1 + 1/(2 + 1/2)
1 + 1/(2 + 1/(2 + 1/2))
"""

def approx(n):
    return 1 + recurseApprox(n)

def recurseApprox(n):
    global count
    if (n == 0):
        return 0
    if (n == 1):
        return Fraction(1,2)
    else:
        ans = Fraction(1,2 + recurseApprox(n-1))
        temp =  1 + ans
        if (len(str(temp.numerator)) > len(str(temp.denominator))):
            count += 1
        return ans


approx(1000)
print(count)




endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
