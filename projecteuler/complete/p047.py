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
from projecteuler.utils.getprimes import getprimes
from collections import defaultdict as dd
startTime = time.clock()

primes = getprimes()

# Turns out I had solved this years ago, I'm not even sure how I did it. Right now my brute force approach, despite
# precomputed primes and memoization, is still just too slow. Inspiration from the thread: use a sieve to enumerate
# primes as you ascend, and also count factors for each number as you go up. Only count up if you are a prime - that 
# is, if you are not a multiple of any previous number. A useful intuition from this solution, one that has avoided me,
# is that not all problems that deal with primes benefit immediately from a precomputed list of primes - sometimes the 
# operation of deducing primality is directly related to another task related to factors. By very quickly typing in
# that good ol getprimes import (I justify my use of it to myself because I wrote it), and then treating that prime list 
# as a first step, I limit myself to thinking in that box of using the list of primes as it is (or a set of those primes).


count_factors = dd(int)
limit = 1000000
for i in range(2,limit):
  num = i
  if count_factors[i] == 0:
    count = 0
    while (num < limit):
      count_factors[num] += 1
      num += i
  else:
    if count_factors[i] == 4:
      count += 1
      if count == 4:
        print(i-3)
        break
    else:
      count = 0
      
 



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
