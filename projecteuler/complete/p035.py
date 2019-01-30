"""
 https://projecteuler.net/problem=35
 Circular primes


 The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime. 
 There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. 
 How many circular primes are there below one million?
"""

import time
startTime = time.perf_counter()



MAXPRIME = 1000000

primes = [True] * MAXPRIME
primes[0] = False
primes[1] = False

for i in range(2,MAXPRIME):
    j = i
    while (j + i < MAXPRIME):
        j += i
        primes[j] = False


def circular(n):
    global primes
    num = str(n)
    for i in range(0,len(num)):
        x = num[i:len(num)]+num[0:i]
        if (not primes[int(x)]):
            return False
    return True

count = 0
for i in range(1,1000000):
    if (circular(i)):
        count += 1

print(count)


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
