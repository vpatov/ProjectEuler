"""
 https://projecteuler.net/problem=91
 Right triangles with integer coordinates

 The points P ( x _1 , y _1 ) and Q ( x _2 , y _2 ) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form \xce\x94OPQ. 

 
 

 There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is, 0 x _1 , y _1 , x _2 , y _2 

 
 

 Given that 0 x _1 , y _1 , x _2 , y _2
"""
import time
from functools import reduce
from operator import mul
startTime = time.clock()

def dot(it1,it2):
  return sum([reduce(mul,nums) for nums in zip(it1,it2)])


count = 0
limit = 51
for x1 in range(0,limit):
  for y1 in range(0,limit):
    if ((x1,y1) == (0,0)):
      continue
    for x2 in range(0,limit):
      for y2 in range(0,limit):
        if((x2,y2) in [(0,0),(x1,y1)]):
          continue
    
        vecs = [( (x1,y1),(x2,y2) ), ( (-x1,-y1),(x2-x1,y2-y1) ), ( (-x2,-y2),(x1-x2,y1-y2) )]
  
        for vec in vecs:
          if not dot(vec[0],vec[1]):
            count += 1
            break

print(count // 2)
endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
