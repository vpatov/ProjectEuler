"""
 https://projecteuler.net/problem=38
 Pandigital multiples

 Take the number 192 and multiply it by each of 1, 2, and 3: 
 192 * 1 = 192 
192 * 2 = 384 
192 * 3 = 576 
 By concatenating each product we get the 1 to 9 pandigital, 192384576.
 We will call 192384576 the concatenated product of 192 and (1,2,3)
 The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
 giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
 What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
 product of an integer with (1,2, ... , n ) where n > 1?
"""

import time
startTime = time.clock()

def pandigital(n):
    n = str(n)
    x = set(n)
    if len(n) == 9 and (len(x)) == 9 and not x.__contains__('0'):
        return True
    return False

def testNum(n):
    testPan =''
    for i in range(1,10):
        testPan += str(n * i)
        if (len(testPan) == 9):
            return (pandigital(testPan),int(testPan))
        elif (len(testPan) > 9):
            return (False,0)

maxNum = 0

for i in range(1,10000):
    current = testNum(i)
    if (current[0]):
        if current[1] > maxNum:
            maxNum = current[1]

print(maxNum)

#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
