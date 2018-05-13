"""
 https://projecteuler.net/problem=45
 Triangular, pentagonal, and hexagonal

 Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

 Triangle
 T_ n = n ( n +1)/2
 1, 3, 6, 10, 15, ...


 Pentagonal
 P_ n = n (3 n -1)/2
 1, 5, 12, 22, 35, ...
 4,7,10,13

 Hexagonal
 H_ n = n (2 n -1)
 1, 6, 15, 28, 45, ...
 5,9,13,17

 It can be verified that T_285 = P_165 = H_143 = 40755. 
 Find the next triangle number that is also pentagonal and hexagonal.
"""

import time
startTime = time.clock()

(tNums, hNums, pNums) = (set(),set(),set())



tN = 286
hN = 144
pN = 166

tNum = int((tN + 1) * tN) // 2
hNum = int((2*hN - 1) * hN)
pNum = int((3 * pN - 1) * pN) // 2

while(True):


    if (tNum == hNum and hNum == pNum ):
        print(tNum)
        break

    if (tNum <= hNum and tNum <= pNum):
        tN += 1
        tNum = int((tN + 1) * tN) // 2

    elif (hNum <= pNum and hNum <= tNum):
        hN += 1
        hNum = int((2*hN - 1) * hN)


    elif (pNum <= hNum and pNum <= tNum):
        pN += 1
        pNum = int((3 * pN - 1) * pN) // 2







endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")