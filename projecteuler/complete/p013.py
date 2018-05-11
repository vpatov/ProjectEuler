"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

https://projecteuler.net/problem=13
"""

import time
from projecteuler.utils.getinput import getinput
startTime = time.clock()

f = getinput(13)

sum = 0
for line in f:
    sum += int(line[0:12])

print(str(sum)[0:10])

endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
