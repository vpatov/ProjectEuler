"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time

startTime = time.perf_counter()

a = 1
b = 2
found = False
while (a < 1000 and not found):
    while (b < 1000):
        if (a**2 + b**2 == (1000-b-a)**2) :
            #print(a,b,(1000-b-a))
            print(a * b * (1000-b - a))
            found = True
            break

        b += 1
    a += 1
    b = a + 1



endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
