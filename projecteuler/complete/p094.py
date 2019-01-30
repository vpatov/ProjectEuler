"""
 https://projecteuler.net/problem=94
 Almost equilateral triangles

 It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units. 
 We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit. 
 Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""
import time
import numpy as np
import math
startTime = time.perf_counter()

# recurrence relation that generates sides of the triangles
# https://oeis.org/A120893
def a(n):
  if n == 0 or n == 1:
    return 1
  if n == 2:
    return 5
  return 3*a(n-1) + 3*a(n-2) - a(n-3)


def calc1(a):
  return math.sqrt((a + 1) * (3*a - 1)) * (a-1) / 4

def calc2(a):
  return math.sqrt((a - 1) * (3*a + 1)) * (a+1) / 4


target = 1e9
sum_perimeters = 0
for i in range(2,20):

  side = a(i)
  a1,a2 = calc1(side), calc2(side)

  if (abs(a1 - int(a1)) < 0.0000001):
    perimeter = side + side + side - 1
    #print('{:15d}{:15d}{:15d}{:15d}{:25.3f}'.format(side,side,side-1,perimeter,a1))
  
  elif (abs(a2 - int(a2)) < 0.0000001):
    perimeter = side + side + side + 1
    #print('{:15d}{:15d}{:15d}{:15d}{:25.3f}'.format(side,side,side+1,perimeter,a2))
 
  if perimeter > target:
    break
  sum_perimeters += perimeter
  
print(sum_perimeters)


endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
