"""
 https://projecteuler.net/problem=53
 Combinatoric selections

 There are exactly ten ways of selecting three from five, 12345: 
 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345 
 In combinatorics, we use the notation, ^5 C_3 = 10. 
 In general, 
 
 ^ n C_ r = 
 n ! r !( n\xe2\x88\x92r )! 
 ,where r n , n ! = n *( n \xe2\x88\x921)*...*3*2*1, and 0! = 1. 
 
 It is not until n = 23, that a value exceeds one-million: ^23 C_10 = 1144066. 
 How many, not necessarily distinct, values of \xc2\xa0^ n C_ r , for 1 n
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
