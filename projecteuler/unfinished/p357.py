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
from functools import reduce
import numpy as np
import itertools
startTime = time.clock()


primes = getprimes()
subset = set(primes[:100000000])
print("Created set of primes")

def getprimefactors(n):
  primefactors = []
  index = 0
  while(n != 1):
    if n % primes[index] == 0:
       n//= primes[index]
       primefactors.append(primes[index])
    else:
      index += 1
  return primefactors

def getdivisors(n):
  primefactors = getprimefactors(n)
  divisors = set([1,n])
  for i in range(1,len(primefactors)):
    for group in itertools.combinations(primefactors,i):
      divisors.add(reduce(np.int64.__mul__,group))
  return divisors

def satisfies(n):
  divisors = getdivisors(n)
  for d in divisors:
    if (d + (n//d)) not in subset:
      return False
  return True


nums = []
for i in range(1,1000):
  if satisfies(i):
    nums.append(i)


for num in nums:
  print((num + 1) % 4)


#code
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
