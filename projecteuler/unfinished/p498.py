"""
 https://projecteuler.net/problem=498
 Remainder of polynomial division

 For positive integers n and m , we define two polynomials F_ n ( x ) = x ^ n and G_ m ( x ) = ( x -1)^ m . 
We also define a polynomial R_ n , m ( x ) as the remainder of the division of F_ n ( x ) by G_ m ( x ). 
For example, R_6,3 ( x ) = 15 x ^2 - 24 x + 10. 

 Let C( n , m , d ) be the absolute value of the coefficient of the d -th degree term of R_ n , m ( x ). 
We can verify that C(6, 3, 1) = 24 and C(100, 10, 4) = 227197811615775. 

 Find C(10^13 , 10^12 , 10^4 ) mod 999999937.
"""
import time
import numpy as np
startTime = time.clock()

#code
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
