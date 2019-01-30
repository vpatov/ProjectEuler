"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as
a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import time

startTime = time.perf_counter()


def pandigital(n):
    n = str(n)
    x = set(n)
    if len(n) == 9 and (len(x)) == 9 and not x.__contains__('0'):
        return True
    return False
def coPan(x,y):
    return len(set(str(x)).intersection(set(str(y)))) == 0

products = set()

for i in range(1,10):
    for j in range(1234,9999):
        if (coPan(i,j)):
            prod = i * j
            if pandigital(str(i) + str(j) + str(prod)):
                products.add(prod)

for i in range(12,99):
    for j in range(123,999):
        if (coPan(i,j)):
            prod = i * j
            if pandigital(str(i) + str(j) + str(prod)):
                products.add(prod)

print(sum(products))

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
