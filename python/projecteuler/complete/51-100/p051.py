"""
 https://projecteuler.net/problem=51
 Prime digit replacements


 By replacing the 1^st digit of the 2-digit number *3, it turns out that
 six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
 By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this 5-digit number
 is the first example having seven primes among the ten generated numbers,
 yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.

 Consequently 56003, being the first member of this family, is the smallest prime with this property.

 Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
 with the same digit, is part of an eight prime value family.

"""

import time
import itertools
import numpy as np
from projecteuler.utils.getprimes import getprimes
startTime = time.perf_counter()

# ignore single-digit primes 2,3,5,7
primes = getprimes()
cutoff = np.argmax(primes > 1000000) - 1
primes = primes[4:cutoff]
primeset = set(primes)
checkedprimes = set()
digits = [str(i) for i in range(10)]


target = 8
corresponding_prime = 0
corresponding_combo = None
candidate_primes = []


def getmin(pr,combo):
  strnum = list(str(pr))
  for digit in digits:
    for index in combo:
      strnum[index] = digit
    intnum = int(''.join(strnum))
    if intnum in primeset:
      return intnum

for p in primeset:
  if p in checkedprimes:
    continue
  
  for i in range(1,len(str(p))):
    combos = list(itertools.combinations(range(len(str(p))),i))
    for combo in combos:
      strnum = list(str(p))
      count_prime_family = 0
      for digit in digits:
        if digit == '0' and 0 in combo:
          continue
        for index in combo:
          strnum[index] = digit
        primenum = int(''.join(strnum))
        if primenum in primeset:
          checkedprimes.add(primenum)
          count_prime_family += 1
      if count_prime_family == target:
        corresponding_prime = p
        corresponding_combo = combo
        candidate_primes.append(getmin(corresponding_prime,corresponding_combo))
        break
 
print(min(candidate_primes)) 
  
endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
