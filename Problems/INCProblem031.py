"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

import time

startTime = time.clock()

#code
numWays = 0
i = 200
while (i >= 0):
    j = i
    while (j >= 0):
        k = j
        while (k >= 0):
            l = k
            while (l >= 0):
                x = 0

print(numWays)


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
