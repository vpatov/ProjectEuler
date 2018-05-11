"""
 https://projecteuler.net/problem=50
 Consecutive prime sum

 The prime 41, can be written as the sum of six consecutive primes: 
 41 = 2 + 3 + 5 + 7 + 11 + 13 
 This is the longest sum of consecutive primes that adds to a prime below one-hundred. 
 The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953. 
 Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import time
startTime = time.clock()






MAXPRIME = 1000000

primes = [True] * MAXPRIME
primes[0] = False
primes[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primes[j] = False


for i in range(0,100000):
    for j in range(0,i):
        print(j,i,sum(range(j, i)))



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
