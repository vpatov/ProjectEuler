"""
 https://projecteuler.net/problem=87
 Prime power triples


 The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way: 
 28 = 2^2 + 2^3 + 2^4 
33 = 3^2 + 2^3 + 2^4 
49 = 5^2 + 2^3 + 2^4 
47 = 2^2 + 3^3 + 2^4 
 How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""
import time
import numpy as np
from projecteuler.utils.getprimes import getprimes
startTime = time.clock()

primes = getprimes()
primes = primes[:np.argmax(primes > np.sqrt(50_000_000))]

target = 50_000_000

squares = np.array([num**2 for num in primes])
cubes = np.array([num**3 for num in primes if num**3 < target])
quads = np.array([num**4 for num in primes if num**4 < target])


numbers = set()
for square in squares:
  for cube in cubes:
    partial = square + cube
    if partial >= target:
      break
    for quad in quads:
      s = partial + quad
      if s > target:
        break
      numbers.add(s)

print(len(numbers))
  


endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
