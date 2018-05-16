"""
 https://projecteuler.net/problem=60
 Prime pair sets


 The primes 3, 7, 109, and 673, are quite remarkable.
 By taking any two primes and concatenating them in any order the result will always be prime.
 For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792,
 represents the lowest sum for a set of four primes with this property.

 Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import time
from projecteuler.utils.getprimes import getprimes, getprimeset
startTime = time.clock()

primes = getprimes()[:100000]
primeset = getprimeset()
print("Created primeset")

nums = ['3','7','109','673']


def get_num():
  for prime in primes:
    if prime in [3,7,109,673]:
      continue
    strnum = str(prime)
    for num in nums:
      c1,c2 = int(strnum + num), int(num + strnum)
      if c1 in primeset and c2 in primeset:
        nums.append(strnum)
        return nums
      else:
        break

print(get_num())
    
    

#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
