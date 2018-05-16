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
import numpy as np
from math import sqrt
from projecteuler.utils.getprimes import getprimes, getprimeset
startTime = time.clock()

primes = getprimes()
primes = [str(p) for p in primes[:np.argmax(primes > 100_000_000)][1:]]
primeset = set(primes)
print("Created primeset")


def memoize(f):
  memo = {}
  def helper(x):
    if x not in memo:            
      memo[x] = f(x)
    return memo[x]
  return helper


@memoize
def is_prime(n):
  num = int(n)
  lim = int(sqrt(num))
  for i in range(3,lim+1,2):
    if num % i == 0:
      return False
  return True

min_sum = float('inf')
min_group = set()

# Each subset of the five primes will be a set that satisfies this property, so we can start by trying to find those.
# We know that 3,7,109, and 673 form such a set. Tacking on a fifth prime to this set, however, creates a set whose sum
# is not actually the minimal sum for a five prime set.

def s(t):
  return sum([int(i) for i in t])

def min_sum(groups):
  return min([s(t) for t in groups])

two_sets = set()
three_sets = set()
four_sets = set()
five_sets = set()

for i in range(0,1500):
  for j in range(i+1,1500):
      
      pi = primes[i]
      pj = primes[j]
      
      if (pi + pj in primeset and pj +pi in primeset):
        two_sets.add((pi,pj))


for pair in two_sets:
  pi,pj = pair
  for k in range(primes.index(pair[-1]),1500):
    pk = primes[k]
    vals = (pi + pk, pj + pk, pk + pi, pk + pj) 
    valid = True
    for val in vals:
      if val not in primeset:
        valid = False
        break
    if valid:
      three_sets.add((pi,pj,pk))


for triplet in three_sets:
  pi,pj,pk = triplet
  for l in range(primes.index(triplet[-1]),1500):
    pl = primes[l]
    vals = (pi + pl, pj + pl, pk + pl, pl + pi, pl + pj, pl + pk)
    valid = True
    for val in vals:
      if val not in primeset:
        valid = False
        break
    if valid:
      four_sets.add((pi,pj,pk,pl))

    
for m in range(0,1500):
  for quad in four_sets:
    
    pi,pj,pk,pl = quad
    pm = primes[m]
    if pm in quad:
      continue

    vals = [p + pm for p in quad] + [pm + p for p in quad]
    valid = True
    for val in vals:
      if val not in primeset:
        valid = False
        break
    if valid:
      five_sets.add((pi,pj,pk,pl,pm))
    

#code

print(min_sum(five_sets))

endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
