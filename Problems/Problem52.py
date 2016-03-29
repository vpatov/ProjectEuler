"""
 https://projecteuler.net/problem=52
 Permuted multiples


 It can be seen that the number, 125874, and its double, 251748,
 contain exactly the same digits, but in a different order.
 Find the smallest positive integer, x , such that 2 x , 3 x , 4 x , 5 x , and 6 x , contain the same digits.
"""

import time
startTime = time.clock()

def eligibleNum(x):
    nums = [str(x*i) for i in range(1,7)]
    digits = set(nums[0])
    for num in nums:
        if (set(num) != digits):
            return False
    return True

i = 1
while(True):
    if (eligibleNum(i)):
        print(i)
        break
    i += 1

endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
