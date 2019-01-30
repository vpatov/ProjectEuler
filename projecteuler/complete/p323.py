"""
 https://projecteuler.net/problem=323
 Bitwise-OR operations on random integers

 Let y _0 , y _1 , y _2 ,... be a sequence of random unsigned 32 bit integers 
(i.e. 0 y_i &lt; 2^32 , every value equally likely). 
 For the sequence x_i the following recursion is given:  x _0 = 0 and 
 x_i = x _ i - 1 | y _ i - 1 , for i &gt; 0. ( | is the bitwise-OR operator) 
 It can be seen that eventually there will be an index N such that x_i = 2^32 -1 (a bit-pattern of all ones) for all i >= N. 

 Find the expected value of N. 
Give your answer rounded to 10 digits after the decimal point.
"""
import time
import numpy as np
startTime = time.perf_counter()


# Probability distribution 
# P(3) = probability that that all bits are set to 1 after 3 random numbers
def P(n):
  return (1 - (1/2)**n)**32 - (1 - (1/2)**(n-1))**32

# Expected value for discrete function is equal to sum(n * P(n)) for all n
# Calculate expected value until first 10 decimal points stop changing

prev = None
s = 0
for n in range(1,100000):
  cur = n*P(n)
  s += cur
  
  if '{:.10f}'.format(s) == prev:
    print(prev)
    break
  prev = '{:.10f}'.format(s)
   




endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
