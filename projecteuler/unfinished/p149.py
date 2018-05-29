"""
 https://projecteuler.net/problem=149
 Searching for a maximum-sum subsequence

 Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1). 

 
 -2 5 3 2 9 -6 5 1 3 2 7 3 -1 8 -4 \xc2\xa0 8  

 Now, let us repeat the search, but on a much larger scale: 

 First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator": 

 For 1 k s _ k = [100003 - 200003 k + 300007 k ^3 ] (modulo 1000000) - 500000. 
For 56 k s _ k = [ s _ k-24 + s _ k-55 + 1000000] (modulo 1000000) - 500000. 

 Thus, s _10 = -393027 and s _100 = 86613. 

 The terms of s are then arranged in a 2000*2000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on. 

 Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
"""
import time
import numpy as np
startTime = time.clock()

#code
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
