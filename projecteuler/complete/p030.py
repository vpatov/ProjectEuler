"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import time

startTime = time.clock()



def canBeWritten(n):
    sumNum = 0
    for digit in str(n):
        sumNum += int(digit) ** 5
    return sumNum == n

sumNums = 0
i = 10
while (i <= 999999):
    if (canBeWritten(i)):
        sumNums += i
    i+=1

print(sumNums)
endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
