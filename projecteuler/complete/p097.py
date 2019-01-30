"""
 https://projecteuler.net/problem=97
 Large non-Mersenne prime

 The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^6972593 -1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^ p -1, have been found which contain more digits. 
 However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433*2^7830457 +1. 
 Find the last ten digits of this prime number.
"""
import time
import numpy as np
startTime = time.perf_counter()

basenum = 28433
num = basenum
p = 1
target = 7830457
num *= 2
while (p < target):
  num *= 2
  p += 1
  num = int(str(num)[-12:])

print(str(num + 1)[-10:])



endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
