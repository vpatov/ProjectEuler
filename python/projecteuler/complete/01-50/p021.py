"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

#names = "a","b","c"
def debugVars(*names):
    statement = 'print('
    for name in names:
        statement += "\'" + name + ":\'," + name + ","
    statement += ')'
    return statement


import time
from math import log,sqrt

startTime = time.perf_counter()

def divisors(n):
    divisors = set([1])
    lim = int(sqrt(n))
    for i in range(2,lim+1):
        if (n % i == 0):
            divisors.add(i)
            divisors.add(int(n/i))
    return divisors


sumDivisors = [0,1]
for i in range(2,10000):
    sumDivisors.append(sum(divisors(i)))



sum = 0
for b in range(0,10000):
    a = sumDivisors[b]
    if (a < 10000):
        if (b == sumDivisors[a] and b != a):
            sum += a

print(sum)

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
