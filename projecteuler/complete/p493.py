"""
 https://projecteuler.net/problem=493
 Under The Rainbow

 70 colored balls are placed in an urn, 10 for each of the seven rainbow colors. 
 What is the expected number of distinct colors in 20 randomly picked balls? 
 Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
import time
import numpy as np
from functools import reduce
from operator import mul
from fractions import Fraction
startTime = time.clock()


def nCk(n,k):
  return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))
print(3 * (1 - (nCk(4,3) / nCk(6,3))))
print('{:.9f}'.format(7 * (1 - (nCk(60,20) / nCk(70,20)))))
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
