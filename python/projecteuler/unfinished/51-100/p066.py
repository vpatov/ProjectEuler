"""
 https://projecteuler.net/problem=66
 Diophantine equation

 Consider quadratic Diophantine equations of the form: 
 x ^2 \xe2\x80\x93 D y ^2 = 1 
 For example, when D=13, the minimal solution in x is 649^2 \xe2\x80\x93 13*180^2 = 1. 
 649^2 – 13×180^2 = 1
 x^2 – Dy^2 = 1
 It can be assumed that there are no solutions in positive integers when D is square. 
 By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following: 
 3^2 \xe2\x80\x93 2*2^2 = 1 
2^2 \xe2\x80\x93 3*1^2 = 1 9 ^2 \xe2\x80\x93 5*4^2 = 1 
5^2 \xe2\x80\x93 6*2^2 = 1 
8^2 \xe2\x80\x93 7*3^2 = 1 
 Hence, by considering minimal solutions in x for D x is obtained when D=5. 
 Find the value of D x for which the largest value of x is obtained.
"""

import time
startTime = time.perf_counter()


#code


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
