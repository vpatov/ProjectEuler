"""
 https://projecteuler.net/problem=37
 Truncatable primes


 The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
 and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
 Find the sum of the only eleven primes that are both truncatable from left to right and right to left. 
 NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import time
import bitstring
from math import log
startTime = time.perf_counter()


MAXPRIME = 1000000

primeBools = [True] * MAXPRIME
primeBools[0] = False
primeBools[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primeBools[j] = False



def truncatable(n):
    num = str(n)
    for i in range(1,len(num)):
        if (not primeBools[int(num[i:len(num)])]):
            return False
        if (not primeBools[int(num[0:len(num)-i])]):
            return False
    return True


sum = 0
count = 0

for i in range(10,len(primeBools)):
    if (count == 11):
        break
    if (primeBools[i] == True):
        if (truncatable(i)):
            sum += i
            count += 1

print(sum)






#code


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
