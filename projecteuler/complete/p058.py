"""
 https://projecteuler.net/problem=58
 Spiral primes

 Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed. 
37 36 35 34 33 32 31
38 17 16 15 14 13 30 
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
 It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting
 is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
 If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
 If this process is continued, what is the side length of the square spiral for which the ratio of primes along both
 diagonals first falls below 10%?
"""

# top left diagonal =       1,5,17,37 -> +4,+12,+20     -> +8
# bottom left diagonal =    1,7,21,43 -> +6,+14,+22     -> +8
# top right diagonal =      1,3,13,31 -> +2,+10,+18     -> +8
# bottom right diagonal =   1,9,25,49 -> +8,+16,+24     -> +8

# we don't have to generate the bottom right diagonal, they are all composite (the odd squares)
import time
startTime = time.clock()

from math import sqrt

#one million
# MAXPRIME = 5000000
#
# primes = [True] * MAXPRIME
# primes[0] = False
# primes[1] = False
#
# for i in range(2,MAXPRIME):
#     j = i
#     while (j + i < MAXPRIME):
#         j += i
#         primes[j] = False

def isPrime(n):
    for i in range(2,int(sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

totalCount = 1
primeCount = 0
sideLength = 1



bottomLeft = [1,6]
topLeft = [1,4]
topRight = [1,2]

diagonals = (bottomLeft,topLeft,topRight)
ratio = 1.0
while (ratio > 0.1):
    for diagonal in diagonals:
        diagonal[0] += diagonal[1]
        diagonal[1] += 8
        if (isPrime(diagonal[0])):
            primeCount += 1
    totalCount += 4
    ratio = primeCount / totalCount
    sideLength += 2

print(sideLength)
endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
