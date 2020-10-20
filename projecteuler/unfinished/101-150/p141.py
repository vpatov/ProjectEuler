"""
 https://projecteuler.net/problem=141
 Investigating progressive numbers, <i>n</i>, which are also square

 A positive integer, n , is divided by d and the quotient and remainder are q and r respectively. In addition d , q , and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order. 
 For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2). 
We will call such numbers, n , progressive. 
 Some progressive numbers, such as 9 and 10404 = 102^2 , happen to also be perfect squares. The sum of all progressive perfect squares below one hundred thousand is 124657. 
 Find the sum of all progressive perfect squares below one trillion (10^12 ).
"""
import time
import numpy as np
startTime = time.perf_counter()

#code
endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
