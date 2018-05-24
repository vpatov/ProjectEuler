import time
from projecteuler.utils.getinput import getinput
startTime = time.clock()


testinput = """- 16  12  21  - - -
16  - - 17  20  - -
12  - - 28  - 31  -
21  17  28  - 18  19  23
- 20  - 18  - - 11
- - 31  19  - - 27
- - - 23  11  27  -"""

#matrix = [[num for num in line.split(' ') if (len(num)!= 0) ] for line in testinput.split('\n')]
#matrix = [[(float('inf') if item == '-' else int(item)) for item in row] for row in matrix]



rawinput = getinput(107).read().strip()
matrix = [[num for num in line.split(',') if (len(num)!= 0) ] for line in rawinput.split('\n')]
matrix = [[(float('inf') if item == '-' else int(item)) for item in row] for row in matrix]

#matrix[i][j] represents the weight of the edge from vertex i to vertex j. Assume that '-' is just an infinite weight edge.



start_weight = sum([sum([num for num in row if num != float('inf')]) for row in matrix]) / 2
visited = set()

vertex = 0
visited = set([vertex])
minimized_weight = 0
while len(visited) != len(matrix):
  mincoor, minedge = (None,None),float('inf')
  for v in visited:
    for index,edge in enumerate(matrix[v]):
      if edge < minedge and index not in visited:
        minedge = edge
        mincoor = (v,index)
    
  visited.add(mincoor[1])
  minimized_weight += minedge

print(int(start_weight - minimized_weight))

endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
