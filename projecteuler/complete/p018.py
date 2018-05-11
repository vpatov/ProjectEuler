"""
Maximum path sum I
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
"""

import time
from projecteuler.utils.getinput import getinput
startTime = time.clock()

f = getinput(18)
grid = []

for line in f:
    line = line.split()
    grid.append([])
    for num in line:
        grid[-1].append(int(num))

i = len(grid) - 2
j = 0
while (i >= 0):
    while (j <= i):
        grid[i][j] = max(grid[i+1][j],grid[i+1][j+1]) + grid[i][j]
        j += 1
    i -= 1
    j = 0

print(grid[0][0])





endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
