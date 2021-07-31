"""
 https://projecteuler.net/problem=357
 Prime generating integers

 
Consider the divisors of 30: 1,2,3,5,6,10,15,30. 
It can be seen that for every divisor d of 30, d +30/ d is prime.
 
 
Find the sum of all positive integers n not exceeding 100 000 000 such that
for every divisor d of n , d + n / d is prime.
"""
import time
from projecteuler.utils.getprimes import getprimes, getprimeset
from functools import reduce
import numpy as np
import itertools
import cProfile
startTime = time.perf_counter()


primes = getprimes()
subset = primes[:np.argmax(primes > 1e8)]
primeset = getprimeset()
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

def factors(n):    
  return set(reduce(list.__add__, 
    ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

def getdivisors(n):
  primefactors = getprimefactors(n)
  divisors = set([1,n])
  for i in range(1,len(primefactors)):
    for group in itertools.combinations(primefactors,i):
      divisors.add(reduce(np.int64.__mul__,group))
  return divisors

def satisfies(n):
  divisors = factors(n)
  for d in divisors:
    r = (d + (n//d)) 
    if r not in primeset:
      return False
  return True


def run():
  nums = []
  for i in range(1,1000000):
    if i in primeset:
      continue
    if satisfies(i):
      nums.append(i)
  return nums


nums = run()

endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
