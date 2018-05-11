"""
 https://projecteuler.net/problem=47
 Distinct primes factors

 The first two consecutive numbers to have two distinct prime factors are: 
 14 = 2 * 7 15 = 3 * 5 
 The first three consecutive numbers to have three distinct prime factors are: 
 644 = 2^2 * 7 * 23, 645 = 3 * 5 * 43, 646 = 2 * 17 * 19.
 Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

import time
startTime = time.clock()

MAXPRIME = 100000

primes = [True] * MAXPRIME
primes[0] = False
primes[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primes[j] = False

primeList = list()
for i in range(0,MAXPRIME):
    if (primes[i]):
        primeList.append(i)



def primeFactors(n):
    factors = set()
    for i in range(0,len(primeList)):
        while (n % primeList[i] == 0):
            factors.add(primeList[i])
            n //= primeList[i]

    return factors

factors = list()

#initialize the prime factors for numbers 1-4
factors.append({})
for i in range(1,4+1):
    factors.append(primeFactors(i))

i = 5
while(i < 10000):
    factors.append(primeFactors(i))

    ##find efficient comparison way

    #print(i)
    i += 1



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
