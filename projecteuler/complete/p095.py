"""
 https://projecteuler.net/problem=95
 Amicable chains

 The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number. 
 Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair. 
 Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers: 
 12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...) 
 Since this chain returns to its starting point, it is called an amicable chain. 
 Find the smallest member of the longest amicable chain with no element exceeding one million.
"""
import time
import numpy as np
import math as math
startTime = time.clock()

target = 1000000

def getdivisors(n) :
  divisors = set([1])       
  # List to store half of the divisors
  for i in range(2, int(math.sqrt(n) + 1)) :
    if (n % i == 0) : 
      divisors.add(int(n/i))
      divisors.add(i)
  return divisors


# the key 220 will have the entry 284
divisor_sum_lookup = dict()

def getchain(number):
  cur = number
  chain  = []
  explored = set()
  length = 0
  prev = None
  while (cur not in explored):
    if cur == 1 or cur > target:
      return 0,None
    chain.append(cur)
    explored.add(cur)

    if cur in divisor_sum_lookup:
      sumdivisors = divisor_sum_lookup[cur]
      return 0,None
    else:
      divisors = getdivisors(cur)
      sumdivisors = sum(divisors)
      divisor_sum_lookup[cur] = sumdivisors
    
    prev = cur
    cur =  sumdivisors
    if cur == prev:
      return 0,None

  chain.append(cur)
  if chain.index(chain[-1]) != len(chain) - 1:
    chain = chain[chain.index(chain[-1]):-1]

  return len(chain),chain
  
longest_length = 0
longest_chain = None
for i in range(2,target):
  length,chain = getchain(i)
  if length > longest_length:
    longest_length = length
    longest_chain = chain

print(min(longest_chain))

endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
