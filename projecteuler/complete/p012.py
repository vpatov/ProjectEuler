"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import time

startTime = time.perf_counter()

from math import log,sqrt

MAXPRIME = 100000

primeBools = [True] * MAXPRIME
primeBools[0] = False
primeBools[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primeBools[j] = False

primes = []
for i in range(0,len(primeBools)):
    if (primeBools[i]):
        primes.append(i)




def divisors(n):
    numDivisors = 1
    lim = int(sqrt(n))
    for i in range(0,lim):
        numRepeats = 0
        while (n % primes[i] == 0):
            numRepeats += 1
            n /= primes[i]
        numDivisors *= (numRepeats + 1)
    return numDivisors


tNums = [1]
index = 1

while(True):
    tNums.append(tNums[index-1] + index+1)
    if (divisors(tNums[index]) >= 500):
        print(tNums[index])
        break
    index +=1



endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
