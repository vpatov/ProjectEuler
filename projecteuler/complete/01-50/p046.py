"""
 https://projecteuler.net/problem=46
 Goldbach\'s other conjecture

 It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square. 
 9 = 7 + 2*1^2 
15 = 7 + 2*2^2 
21 = 3 + 2*3^2 
25 = 7 + 2*3^2 
27 = 19 + 2*2^2 
33 = 31 + 2*1^2 
 It turns out that the conjecture was false. 
 What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import time
startTime = time.perf_counter()


MAXPRIME = 100000

primes = [True] * MAXPRIME
primes[0] = False
primes[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primes[j] = False

squareList = list(2*(i**2) for i in range(0,1000))
squareSet = set(squareList)

def canBeWritten(n):
    i = 0
    currentSquare = squareList[i]

    while (currentSquare < n):
        if (primes[n - currentSquare]):
            return True
        else:
            i += 1
            currentSquare = squareList[i]
    return False

i = 3
while(True):
    if (not canBeWritten(i)):
        print(i)
        break
    i += 2

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
