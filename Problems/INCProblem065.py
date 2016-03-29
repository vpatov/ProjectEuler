"""
 https://projecteuler.net/problem=65
 Convergents of e

 The square root of 2 can be written as an infinite continued fraction. 
 
 \xe2\x88\x9a2 = 1 + 
 1 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 2 + ... 
 
 The infinite continued fraction can be written, \xe2\x88\x9a2 = [1;(2)], (2) indicates that 2 repeats ad infinitum . In a similar way, \xe2\x88\x9a23 = [4;(1,3,1,8)]. 
 It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for \xe2\x88\x9a2. 
 

 1 + 
 1 
 = 3/2 
 \xc2\xa0 
 2 
 \xc2\xa0 
  1 + 
 1 
 = 7/5 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 2 
 \xc2\xa0 
  1 + 
 1 
 = 17/12 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 2 
 \xc2\xa0 
  1 + 
 1 
 = 41/29 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 2 
 \xc2\xa0 
 
 Hence the sequence of the first ten convergents for \xe2\x88\x9a2 are: 
 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ... 
 What is most surprising is that the important mathematical constant, e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2 k ,1, ...]. 
 The first ten terms in the sequence of convergents for e are: 
 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ... 
 The sum of digits in the numerator of the 10^th convergent is 1+4+5+7=17. 
 Find the sum of digits in the numerator of the 100^th convergent of the continued fraction for e .
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
