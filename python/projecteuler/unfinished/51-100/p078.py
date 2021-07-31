"""
 https://projecteuler.net/problem=78
 Coin partitions

 Let p( n ) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7. 
 
 OOOOO 
 OOOO\xc2\xa0 \xc2\xa0O 
 OOO\xc2\xa0 \xc2\xa0OO 
 OOO\xc2\xa0 \xc2\xa0O\xc2\xa0 \xc2\xa0O 
 OO\xc2\xa0 \xc2\xa0OO\xc2\xa0 \xc2\xa0O 
 OO\xc2\xa0 \xc2\xa0O\xc2\xa0 \xc2\xa0O\xc2\xa0 \xc2\xa0O 
 O\xc2\xa0 \xc2\xa0O\xc2\xa0 \xc2\xa0O\xc2\xa0 \xc2\xa0O\xc2\xa0 \xc2\xa0O 
 
 Find the least value of n for which p( n ) is divisible by one million.
"""

import time
startTime = time.perf_counter()


#code


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
