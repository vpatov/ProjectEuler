"""
 https://projecteuler.net/problem=61
 Cyclical figurate numbers

 Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae: 
 Triangle 
 \xc2\xa0 
 P_3, n = n ( n +1)/2 
 \xc2\xa0 
 1, 3, 6, 10, 15, ... 
 Square 
 \xc2\xa0 
 P_4, n = n ^2 
 \xc2\xa0 
 1, 4, 9, 16, 25, ... 
 Pentagonal 
 \xc2\xa0 
 P_5, n = n (3 n -1)/2 
 \xc2\xa0 
 1, 5, 12, 22, 35, ... 
 Hexagonal 
 \xc2\xa0 
 P_6, n = n (2 n -1) 
 \xc2\xa0 
 1, 6, 15, 28, 45, ... 
 Heptagonal 
 \xc2\xa0 
 P_7, n = n (5 n -3)/2 
 \xc2\xa0 
 1, 7, 18, 34, 55, ... 
 Octagonal 
 \xc2\xa0 
 P_8, n = n (3 n -2) 
 \xc2\xa0 
 1, 8, 21, 40, 65, ... 
 The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties. 
 The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first). 
 Each polygonal type: triangle (P_3,127 =8128), square (P_4,91 =8281), and pentagonal (P_5,44 =2882), is represented by a different number in the set. 
 This is the only set of 4-digit numbers with this property. 
 Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
