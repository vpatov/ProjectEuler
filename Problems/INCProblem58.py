"""
 https://projecteuler.net/problem=58
 Spiral primes

 Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed. 
 37 36 35 34 33 32 31 
38 17 16 15 14 13 30 
39 18 \xc2\xa0 5 \xc2\xa04 \xc2\xa0 3 12 29 
40 19 \xc2\xa06 \xc2\xa01 \xc2\xa02 11 28 
41 20 \xc2\xa0 7 \xc2\xa08 \xc2\xa09 10 27 
42 21 22 23 24 25 26 43 44 45 46 47 48 49 
 It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 \xe2\x89\x88 62%. 
 If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
