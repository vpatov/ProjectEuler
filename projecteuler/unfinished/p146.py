"""
 https://projecteuler.net/problem=146
 Investigating a Prime Pattern 

 The smallest positive integer n for which the numbers n ^2 +1, n ^2 +3, n ^2 +7, n ^2 +9, n ^2 +13, and n ^2 +27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490. 

 What is the sum of all such integers n below 150 million?
"""
import time
import numpy as np
from projecteuler.utils.getprimes import getprimes
startTime = time.perf_counter()

target = 150_000_000

primes = getprimes()
primes = primes[:np.argmax(primes > target)]

lim = int((target - 1)**(1/2))
nums = set([n**2 + 1 for n in range(1,lim)])
targetdiffs = np.array([2,4,2,4,14]).astype(np.int64)  # difference between n^2 + 1 and each of the following primes
diffs = np.zeros(len(primes)).astype(np.int64)

print("Created number arrays")

for i in range(1,len(diffs)):
  diffs[i] = primes[i] - primes[i-1]

res = diffs.tostring().index(targetdiffs.tostring()) // diffs.itemsize

dstr = diffs.tostring()
tdstr = targetdiffs.tostring()

indeces = []
def getindex(ind):
  return dstr.index(tdstr,ind*diffs.itemsize) // diffs.itemsize

i = 0
while (True):
  try:
    ind = getindex(i)
    indeces.append(ind)
    i = ind + 1
  except:
    break

for ind in indeces:
  if primes[ind-1] in nums:
    print(ind-1,primes[ind-1])


endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
