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
import numpy as np
from projecteuler.utils.getprimes import getprimes
startTime = time.clock()







primes = getprimes()
cutoff = np.argmax(primes > 1000000)
primes = primes[:cutoff]
primeset = set(primes)


window_start = 0
longest_sequence = 0
corresponding_prime = 0

for window in range(2,100):
  init_sum = np.sum(primes[:window])
  current_sum = init_sum
  for index in range(0,cutoff-window):
    if current_sum in primeset:
      longest_sequence = window
      corresponding_prime = current_sum
      window_start = index
    current_sum -= primes[index]
    current_sum += primes[index+window]

# print(longest_sequence)
# print(window_start)
print(corresponding_prime)


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
