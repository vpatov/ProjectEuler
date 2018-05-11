"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import time

startTime = time.clock()

def oneLongDivBy(n):
    quot = '0.'
    if (10 % n == 0):
        quot += str(10 // n)
    elif (100 % n == 0):
        print()


def lenRecurCycle(n):
    num = str(n)[2:]
    length = 0
    maxLength = 0
    if len(set(list(num))) == 1:
        return 1
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if (num[j:].__contains__(num[i:j])):
                length += 1

        if (length > maxLength):
            maxLength = length
        length = 0

    return maxLength

max = 1
maxD = 1
for i in range(1,1000):
    term = lenRecurCycle(1/i)
    print(i,term,1/i)
    if (term > max):
        max = term
        maxD = i

print((max,maxD))
endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
