"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import time

startTime = time.perf_counter()

prod = 1 * 2 * 3 *5 * 7 * 11 * 13 * 17 * 19
next = [4,6,8,9,10,13,14,15,16,18]

#check if n is divisible by 1 , ... , limit
def checkDivisibility(n,limit):
    for i in range(2,limit+1):
        if (n % i != 0):
            return False

    return True



index = 0
while (not checkDivisibility(prod,20)):
    prod *= next[index]
    index += 1
print(prod)

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
