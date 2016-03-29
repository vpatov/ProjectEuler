"""
 https://projecteuler.net/problem=56
 Powerful digit sum


 A googol (10^100 ) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large:
 one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

 Considering natural numbers of the form, a^b , where a, b < 100, what is the maximum digital sum?
"""

import time
startTime = time.clock()

maxSum = 0
for a in range(1,100):
    for b in range(1,100):
        val = (sum(int(digit) for digit in (str(a**b))))
        if val > maxSum:
            maxSum = val

print(maxSum)
endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
