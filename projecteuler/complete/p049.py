"""
 https://projecteuler.net/problem=49
 Prime permutations

 The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another. 
 There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence. 
 What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import time
startTime = time.perf_counter()

MAXPRIME = 10000

primes = [True] * MAXPRIME
primes[0] = False
primes[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primes[j] = False

for i in range(0,10000 - (6660)):
    if (i == 1487):
        continue
    if primes[i]:
        if (primes[i+3330] and primes[i+6660]):
            if set(str(i)) == set(str(i+3330)) and set(str(i+3330)) == set(str(i+6660)):
                print(str(i)+str(i+3330)+str(i+6660))
                break


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
