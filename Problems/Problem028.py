"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import time

startTime = time.clock()

#numbers on diagonals = 1 ,     3,5,7,9,     13,17,21,25
#                       1x1     3x3             5x5

step = 2
sumNums = 1
currentNum = 1
i = 0
n = 1001
while (i < (n-1)*2):
    currentNum += step
    sumNums += currentNum
    i+=1
    if (i % 4 == 0):
        step += 2

print(sumNums)



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
