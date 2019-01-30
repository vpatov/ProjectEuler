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

startTime = time.perf_counter()


def get_digits(num):
  visited = set()
  res = ['0','.'] + ['0']*10000
  divisor = num
  current = 10
  index = 2
  while (divisor > current):
    current *= 10
    index += 1
    
  start_index = index -1
  
  while(True):
    if current in visited:
      break
    if index >= len(res):
      break
    add = current // divisor
    res[index] = str(add)
    index += 1
    #res += str(add)
    visited.add(current)
    assert(current - (divisor * (current // divisor)) == current % divisor)
    current %= divisor
    if current == 0:
      break
    current *= 10
    while(current < divisor):
      current *= 10
      index += 1
    
  return ''.join(res)[:index],index - start_index

maxlen = 0
maxres = None
for d in range(1,1000):
  res,l = get_digits(d)
  if l > maxlen:
    maxlen = l
    maxres = res

print(maxlen)
endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
