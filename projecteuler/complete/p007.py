"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

import time
import bitstring
from math import log


startTime = time.perf_counter()

primes = []
goal = 10001
limit = int(goal * (log(goal) + 10))
primeBools = bitstring.BitArray()
primeBools.append(limit)
primeBools[0] = 1
primeBools[1] = 1
for i in range(2,limit):
    j = i
    while (j + i< limit):
        j += i
        #set prime values of j to True in the boolean bitstring array
        primeBools[j] = True


for i in range(0,len(primeBools)):
    if (primeBools[i] != 1):
        primes.append(i)

print(primes[10001 - 1])



endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
