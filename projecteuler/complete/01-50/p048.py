"""
 https://projecteuler.net/problem=48
 Self powers


 The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317. 
 Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 .
"""

import time
startTime = time.perf_counter()


print(str(sum(i**i for i in range(1,1000)))[-10:])

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
