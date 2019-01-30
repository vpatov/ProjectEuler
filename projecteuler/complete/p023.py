"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to
the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be
reduced any further by analysis even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

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

divisors = [divisors(i) for i in range(28124)]

def abundant(n):
    return sum(divisors[n]) > n

abundants = set()
for i in range(1,28124):
    if (abundant(i)):
        abundants.add(i)


def cannotBeWritten(n):
    for i in abundants:
        if (i > n):
            return True
        if (abundants.__contains__(n - i)):
            return False
    return True


print(sum(filter((cannotBeWritten),range(28214))))

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
