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


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
