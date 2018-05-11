"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time

startTime = time.clock()


MAXPRIME = 2000000

primes = [True] * MAXPRIME
primes[0] = False
primes[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primes[j] = False

index = 0
sum = 0
while (index < MAXPRIME):
    if (primes[index]):
        sum += index
    index +=1

print(sum)


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
