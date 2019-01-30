"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

startTime = time.perf_counter()

lengths = dict()

def computeLength(input):
    global lengths
    count = 1
    n = input
    while (n > 1):
        if (lengths.__contains__(n)):
            lengths[input] = count-1 + lengths[n]
            return count-1 + lengths[n]
        if (n % 2 == 0):
            n /= 2
        else :
            n = 3*n + 1
        count += 1

    lengths[input] = count
    return count

longest = 1
longestStarting = 1
for i in range(0,1000000):
    length = computeLength(i)
    if (length > longest):
        longest = length
        longestStarting = i

print(longestStarting)



endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
