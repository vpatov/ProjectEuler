"""
 https://projecteuler.net/problem=80
 Square root digital expansion


 It is well known that if the square root of a natural number is not an integer, then it is irrational.
 The decimal expansion of such square roots is infinite without any repeating pattern at all.
 The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475. 
 For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
 for all the irrational square roots.
"""

import time
from decimal import *
startTime = time.clock()

#set the precision a little bit past 100
getcontext().prec = 102


#dont check the squares
squares = set([4,9,16,25,36,49,64,81,100])
#awesome python one liner :)
print(sum(sum(int(i) for i in (str((Decimal(str(j))).sqrt()))[:101]  if i.isnumeric()) for j in range(2,100) if j not in squares))



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
