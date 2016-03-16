"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/problem=15

How many such routes are there through a 20×20 grid?
"""

import time

startTime = time.clock()

size = 20

### Recursive Solution using a dictionary for memoization
ways = dict()
def count():
    return countWays(0,0,size)

def countWays(i,j,size):
    if (ways.__contains__((i,j))):
        return ways[(i,j)]
    if i > size or j > size:
        return 0
    if (i,j) == (size,size):
        return 1
    else:
        temp1 = countWays(i+1,j,size)
        temp2 = countWays(i,j+1,size)
        ways[(i+1,j)] = temp1
        ways[(i,j+1)] = temp2
        return temp1 + temp2
print(count())



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
