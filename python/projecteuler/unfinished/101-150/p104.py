import time
import numpy as np
startTime = time.perf_counter()

limit = 100_000
nums = [0] * limit

nums[0] = 0
nums[1] = 1
nums[2] = 1

for i in range(3,len(nums)):
  nums[i] = nums[i-1] + nums[i-2]

refset = set([str(i) for i in range(1,10)])

def satisfies(num):
  strnum = str(num)
  return set(strnum[0:9]) == refset and set(strnum[-9:]) == refset
  


def satisfies2(num):
  strnum = str(num)
  firstdigits = set(strnum[0:9])
  return firstdigits == refset
 
for i in range(0,len(nums)):
  if satisfies(nums[i]):
    print(i,nums[i])
    break

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")

