"""
 https://projecteuler.net/problem=81
 Path sum: two ways

 In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
 by only moving to the right and down , is indicated in bold red and is equal to 2427.
 

 
 Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file
 containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

import time
from projecteuler.utils.getinput import getinput
startTime = time.clock()



size = 80
f = getinput(81)
mat = []
i = 0
j = 0
for line in f:
    nums = line.split(",")
    mat.append(nums)

for i in range(0,size):
    for j in range(0,size):
        mat[i][j] = int(mat[i][j])

row = size - 1
col = size - 1

while (col >= 0):
    while (row >= 0):
        if (row == size - 1 and col == size - 1):
            row-= 1
            continue

        if (row == size - 1 and col != size - 1):
            mat[row][col] += mat[row][col+1]

        if (col == size - 1 and row != size - 1):
            mat[row][col] += mat[row+1][col]

        if (col != size - 1 and row != size - 1):
            if (mat[row+1][col] < mat[row][col+1]):
                mat[row][col] += mat[row+1][col]
            else:
                mat[row][col] += mat[row][col+1]

        row -=1


    col -=1
    row = size - 1

print(mat[0][0])





endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
