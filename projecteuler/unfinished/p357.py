"""
 https://projecteuler.net/problem=357
 Prime generating integers

 
Consider the divisors of 30: 1,2,3,5,6,10,15,30. 
It can be seen that for every divisor d of 30, d +30/ d is prime.
 
 
Find the sum of all positive integers n not exceeding 100 000 000 such that
for every divisor d of n , d + n / d is prime.
"""
import time
from projecteuler.utils.getprimes import getprimes
import numpy as np
import itertools
startTime = time.clock()


primes = getprimes()
subset = primes[:10]



#code
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
