"""
It seems that prime number generation is a frequently reoccurring subtask when solving Project Euler problems...
I've been using the Sieve of Erastosthenes, which is relatively efficient O(N * log (log N)), but I just read that the Sieve of Atkin
can perform faster, in O(N) time. So I'm going to take the algorithm from the wikipedia page -

     "https://en.wikipedia.org/wiki/Sieve_of_Atkin"
"""



import math
import time
import sys
import json
import os
import numpy as np

def sieve_atkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

def sieve_atkin_nump(limit):
  pass 


if __name__ == '__main__':
  startTime = time.clock()
  
  limit = int(sys.argv[1])  

  if len(sys.argv) == 3:
    target_dir = sys.argv[2]
  else:
    target_dir = '.'


  primes = np.array(sieve_atkin(limit))
  filename = 'primes' + '1e' + str(len(str(limit))) + '.npy'

  with open(os.path.join(target_dir,filename),'wb') as f:
    np.save(f,primes)
  endTime = time.clock()
  print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")




