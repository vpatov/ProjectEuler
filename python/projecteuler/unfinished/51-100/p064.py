"""
 https://projecteuler.net/problem=64
 Odd period square roots

 All square roots are periodic when written as continued fractions and can be written in the form: 
 
 \xe2\x88\x9a N = a _0 + 
 1 
 \xc2\xa0 
 a _1 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 a _2 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 a _3 + ... 
 
 For example, let us consider \xe2\x88\x9a23: 
 
 \xe2\x88\x9a23 = 4 + \xe2\x88\x9a23 \xe2\x80\x94 4 = 4 +\xc2\xa0 
 1 
 \xc2\xa0= 4 +\xc2\xa0 
 1 
 \xc2\xa0 
 1 \xe2\x88\x9a23\xe2\x80\x944 
 \xc2\xa0 
 1 +\xc2\xa0 
 \xe2\x88\x9a23 \xe2\x80\x93 3 7 
 
 If we continue we would get the following expansion: 
 
 \xe2\x88\x9a23 = 4 + 
 1 
 \xc2\xa0 
 1 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 3 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 1 + 
 1 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 \xc2\xa0 
 8 + ... 
 
 The process can be summarised as follows: 
 
 a _0 = 4, 
 \xc2\xa0 
 1 \xe2\x88\x9a23\xe2\x80\x944 
 \xc2\xa0=\xc2\xa0 
 \xe2\x88\x9a23+4 7 
 \xc2\xa0=\xc2\xa01 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x943 7 
 a _1 = 1, 
 \xc2\xa0 
 7 \xe2\x88\x9a23\xe2\x80\x943 
 \xc2\xa0=\xc2\xa0 
 7(\xe2\x88\x9a23+3) 14 
 \xc2\xa0=\xc2\xa03 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x943 2 
 a _2 = 3, 
 \xc2\xa0 
 2 \xe2\x88\x9a23\xe2\x80\x943 
 \xc2\xa0=\xc2\xa0 
 2(\xe2\x88\x9a23+3) 14 
 \xc2\xa0=\xc2\xa01 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x944 7 
 a _3 = 1, 
 \xc2\xa0 
 7 \xe2\x88\x9a23\xe2\x80\x944 
 \xc2\xa0=\xc2\xa0 
 7(\xe2\x88\x9a23+4) 7 
 \xc2\xa0=\xc2\xa08 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x944 
 a _4 = 8, 
 \xc2\xa0 
 1 \xe2\x88\x9a23\xe2\x80\x944 
 \xc2\xa0=\xc2\xa0 
 \xe2\x88\x9a23+4 7 
 \xc2\xa0=\xc2\xa01 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x943 7 
 a _5 = 1, 
 \xc2\xa0 
 7 \xe2\x88\x9a23\xe2\x80\x943 
 \xc2\xa0=\xc2\xa0 
 7(\xe2\x88\x9a23+3) 14 
 \xc2\xa0=\xc2\xa03 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x943 2 
 a _6 = 3, 
 \xc2\xa0 
 2 \xe2\x88\x9a23\xe2\x80\x943 
 \xc2\xa0=\xc2\xa0 
 2(\xe2\x88\x9a23+3) 14 
 \xc2\xa0=\xc2\xa01 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x944 7 
 a _7 = 1, 
 \xc2\xa0 
 7 \xe2\x88\x9a23\xe2\x80\x944 
 \xc2\xa0=\xc2\xa0 
 7(\xe2\x88\x9a23+4) 7 
 \xc2\xa0=\xc2\xa08 +\xc2\xa0 
 \xe2\x88\x9a23\xe2\x80\x944 
 
 It can be seen that the sequence is repeating. For conciseness, we use the notation \xe2\x88\x9a23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely. 

 The first ten continued fraction representations of (irrational) square roots are: 
 \xe2\x88\x9a2=[1;(2)], period=1 
\xe2\x88\x9a3=[1;(1,2)], period=2 
\xe2\x88\x9a5=[2;(4)], period=1 
\xe2\x88\x9a6=[2;(2,4)], period=2 
\xe2\x88\x9a7=[2;(1,1,1,4)], period=4 
\xe2\x88\x9a8=[2;(1,4)], period=2 
\xe2\x88\x9a10=[3;(6)], period=1 
\xe2\x88\x9a11=[3;(3,6)], period=2 
\xe2\x88\x9a12= [3;(2,6)], period=2 
\xe2\x88\x9a13=[3;(1,1,1,1,6)], period=5 
 Exactly four continued fractions, for N 
 How many continued fractions for N
"""

import time
startTime = time.perf_counter()


#code


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")