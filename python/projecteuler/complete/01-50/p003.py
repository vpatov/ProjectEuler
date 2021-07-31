"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import time
startTime = time.perf_counter()


from math import sqrt
from math import ceil

NUMBER = 600851475143
MAXPRIME = ceil(sqrt(NUMBER))

primes = [True] * MAXPRIME
primes[0] = False
primes[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primes[j] = False

index = MAXPRIME - 1
while (index > 0):
    if (primes[index]):
        if (NUMBER % index == 0):
            print(index)
            break
    index -= 1


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
