"""
 https://projecteuler.net/problem=148
 Exploring Pascal\'s triangle

 We can easily verify that none of the entries in the first seven rows of Pascal\'s triangle are divisible by 7: 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa02 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa03 
 \xc2\xa0 
 \xc2\xa03 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa04 
 \xc2\xa0 
 \xc2\xa06 
 \xc2\xa0 
 \xc2\xa04 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa01 
 \xc2\xa0 
 \xc2\xa05 
 \xc2\xa0 
 10 
 \xc2\xa0 
 10 
 \xc2\xa0 
 \xc2\xa05 
 \xc2\xa0 
 \xc2\xa01 
 1 
 \xc2\xa0 
 \xc2\xa06 
 \xc2\xa0 
 15 
 \xc2\xa0 
 20 
 \xc2\xa0 
 15 
 \xc2\xa0 
 \xc2\xa06 
 \xc2\xa0 
 \xc2\xa01 
 However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7. 

 Find the number of entries which are not divisible by 7 in the first one billion (10^9 ) rows of Pascal\'s triangle.
"""
import time
import numpy as np
startTime = time.clock()

#code
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
