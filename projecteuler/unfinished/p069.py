"""
 https://projecteuler.net/problem=69
 Totient maximum


 Euler\'s Totient function, \xcf\x86( n ) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n . For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, \xcf\x86(9)=6. 
 
  n 
 Relatively Prime 
 \xcf\x86( n ) 
 n /\xcf\x86( n ) 
 2 
 1 
 1 
 2 
 3 
 1,2 
 2 
 1.5 
 4 
 1,3 
 2 
 2 
 5 
 1,2,3,4 
 4 
 1.25 
 6 
 1,5 
 2 
 3 
 7 
 1,2,3,4,5,6 
 6 
 1.1666... 
 8 
 1,3,5,7 
 4 
 2 
 9 
 1,2,4,5,7,8 
 6 
 1.5 
 10 
 1,3,7,9 
 4 
 2.5 
 
 It can be seen that n =6 produces a maximum n /\xcf\x86( n ) for n 
 Find the value of n n /\xcf\x86( n ) is a maximum.
"""

import time
startTime = time.perf_counter()


#code


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
