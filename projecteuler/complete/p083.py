"""
 https://projecteuler.net/problem=83
 Path sum: four ways

 NOTE: This problem is a significantly more challenging version of Problem 81 . 
 In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297. 
 
$$
\\begin{pmatrix}
\\color{red}{131} &amp; 673 &amp; \\color{red}{234} &amp; \\color{red}{103} &amp; \\color{red}{18}\\\\
\\color{red}{201} &amp; \\color{red}{96} &amp; \\color{red}{342} &amp; 965 &amp; \\color{red}{150}\\\\
630 &amp; 803 &amp; 746 &amp; \\color{red}{422} &amp; \\color{red}{111}\\\\
537 &amp; 699 &amp; 497 &amp; \\color{red}{121} &amp; 956\\\\
805 &amp; 732 &amp; 524 &amp; \\color{red}{37} &amp; \\color{red}{331}
\\end{pmatrix}
$$

 
 Find the minimal path sum, in matrix.txt (right click and 
"Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
"""

import time
from projecteuler.utils.getinput import getinput
from queue import PriorityQueue
startTime = time.clock()

def pm(m):
  for row in m:
    print('-------'*len(row))
    for num in row:
      print('{:4d} | '.format(num),end='')
    print()
  print(('-------'*len(m[-1])))


matrix = [[int(num) for num in line.split(',')] for line in getinput(83).readlines()]

test_input = """131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331"""

test_matrix = [[int(num) for num in line.split()] for line in test_input.split('\n')]
test_sum = 2297

m = matrix

#cost_matrix = [[0 for num in row] for row in m]
pq = PriorityQueue()
visited = set()

row,col = 0,0
cost = m[0][0]

pq.put((cost,row,col))
visited.add((row,col))
while(True):
  cost,row,col = pq.get()
  visited.add((row,col))
  #print(cost,":",(row,col))
  if (row,col) == (len(m)-1,len(m)-1):
    print(cost)
    break
  for neighbor in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
    row,col = neighbor
    if (row >= 0 and row < len(m) and col >= 0 and col < len(m)):
      if (row,col) not in visited:
        pq.put((m[row][col] + cost,row,col))

  
      

  




endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
