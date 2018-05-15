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
from queue import PriorityQueue
startTime = time.clock()


def inbounds(matrix,coors):
  row,col = coors
  return not (row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix))

test_matrix = [
  [161,673,234,103,18],
  [201,96,342,965,150],
  [630,803,746,422,111],
  [537,699,497,121,956],
  [805,732,524,37,331]
]


matrix = [[int(num) for num in line.split(',')] for line in getinput(82).readlines()]
test_length = 10
matrix = [row[:test_length] for row in matrix[:test_length]]

search_queue = PriorityQueue()

for row in range(0,len(matrix)):
  search_queue.put((matrix[row][0],row,0))

while(True):
  distance,row,col = search_queue.get()
  if col == len(matrix) - 1:
    print(distance)
    break

  candidates = [(row+1,col),(row-1,col),(row,col+1)]  
  for candidate in candidates:
    if inbounds(matrix,candidate):
      row,col = candidate
      search_queue.put((matrix[row][col] + distance,row,col))




# Idea - perform A* search. Start from anywhere in left column, and end anywhere in right, and find minimal path sum.
# With this, you know for sure that the first column will only have one entry, as will the last.






endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
