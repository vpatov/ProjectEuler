"""
 https://projecteuler.net/problem=150
 Searching a triangular array for a sub-triangle having minimum-sum

 In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible. 
 In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of -42. 
 
 
 We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers s_k in the range \xc2\xb12^19 , using a type of random number generator (known as a Linear Congruential Generator) as follows: 
 t := 0
 
for k = 1 up to k = 500500:
 
\xc2\xa0 \xc2\xa0 t := (615949* t + 797807) modulo 2^20 
\xc2\xa0 \xc2\xa0 s_k := t -2^19 
 Thus: s_1 = 273519, s_2 = -153582, s_3 = 450905 etc 
 Our triangular array is then formed using the pseudo-random numbers thus: 
 
s_1 
s_2 \xc2\xa0 s_3 
s_4 \xc2\xa0 s_5 \xc2\xa0 s_6 \xc2\xa0 
 
s_7 \xc2\xa0 s_8 \xc2\xa0 s_9 \xc2\xa0 s_10 
...
 
 Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).
 
The "sum of a sub-triangle" is defined as the sum of all the elements it contains.
 
Find the smallest possible sub-triangle sum.
"""
import time
import numpy as np
startTime = time.clock()

#code
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
