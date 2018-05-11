"""
 https://projecteuler.net/problem=70
 Totient permutation

 Euler\'s Totient function, \xcf\x86( n ) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n . For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, \xcf\x86(9)=6. The number 1 is considered to be relatively prime to every positive number, so \xcf\x86(1)=1. 
 Interestingly, \xcf\x86(87109)=79180, and it can be seen that 87109 is a permutation of 79180. 
 Find the value of n , 1 &lt; n &lt; 10^7 , for which \xcf\x86( n ) is a permutation of n and the ratio n /\xcf\x86( n ) produces a minimum.
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
