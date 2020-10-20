"""
 https://projecteuler.net/problem=82
 Path sum: three ways

 NOTE: This problem is a more challenging version of Problem 81 . 
 The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994. 
 
$$
\\begin{pmatrix}
131 &amp; 673 &amp; \\color{red}{234} &amp; \\color{red}{103} &amp; \\color{red}{18}\\\\
\\color{red}{201} &amp; \\color{red}{96} &amp; \\color{red}{342} &amp; 965 &amp; 150\\\\
630 &amp; 803 &amp; 746 &amp; 422 &amp; 111\\\\
537 &amp; 699 &amp; 497 &amp; 121 &amp; 956\\\\
805 &amp; 732 &amp; 524 &amp; 37 &amp; 331
\\end{pmatrix}
$$
 
 Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
"""

import time
from projecteuler.utils.getinput import getinput
startTime = time.perf_counter()

def pm(m):
  for row in m:
    for num in row:
      print('{:3d}'.format(num),end=' ')
    print()

test_matrix1 = [
  [161,673,234,103,18],
  [201,96,342,965,150],
  [630,803,746,422,111],
  [537,699,497,121,956],
  [805,732,524,37,331]
]

test_matrix2 = [
  [10,4,3,5],
  [15,2,2,6],
  [9,3,0,1],
  [7,1,4,8]
]


matrix = [[int(num) for num in line.split(',')] for line in getinput(82).readlines()]
# test_length = 10
# matrix = [row[:test_length] for row in matrix[:test_length]]
# matrix = test_matrix1


cost_matrix = [[0 for num in row] for row in matrix]
# initialize first column of cost matrix
for row in range(0,len(cost_matrix)):
  cost_matrix[row][0] = matrix[row][0]


# populate cost_matrix
for col in range(1,len(cost_matrix)):
  for row in range(0,len(cost_matrix)):
    cost_matrix[row][col] = cost_matrix[row][col-1] + matrix[row][col]
  
  while(True):
    changed = False
    for row in range(0,len(cost_matrix)):
      if row == 0:
        if cost_matrix[row][col] - matrix[row][col] > cost_matrix[row+1][col]:
          changed = True
          cost_matrix[row][col] = cost_matrix[row+1][col] + matrix[row][col]
      elif row == len(cost_matrix) - 1:
        if cost_matrix[row][col] - matrix[row][col] > cost_matrix[row-1][col]:
          changed = True
          cost_matrix[row][col] = cost_matrix[row-1][col] + matrix[row][col]
      else:
        new_val = min(cost_matrix[row-1][col],cost_matrix[row+1][col])
        if cost_matrix[row][col] - matrix[row][col] > new_val:
          changed = True
          cost_matrix[row][col] = new_val + matrix[row][col]
    if not changed:
      break



print(min([row[-1] for row in cost_matrix]))
  






endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
