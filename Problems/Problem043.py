"""
 https://projecteuler.net/problem=43
 Sub-string divisibility

 The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property. 
 Let d _1 be the 1^st digit, d _2 be the 2^nd digit, and so on. In this way, we note the following: 
 d _2 d _3 d _4 =406 is divisible by 2 
 d _3 d _4 d _5 =063 is divisible by 3 
 d _4 d _5 d _6 =635 is divisible by 5 
 d _5 d _6 d _7 =357 is divisible by 7 
 d _6 d _7 d _8 =572 is divisible by 11 
 d _7 d _8 d _9 =728 is divisible by 13 
 d _8 d _9 d _10 =289 is divisible by 17 
 Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import time
import itertools
startTime = time.clock()

perms = itertools.permutations("1234576890")


def isValid(perm):
    perm = str(perm)
    if (int(perm[-1]) % 2 == 0):
        return False

    if (int(perm[-3:]) % 17 != 0):
        return False

    if (int(perm[-4:-1]) % 13 != 0):
        return False

    if (int(perm[-5:-2]) % 11 != 0):
        return False

    if (int(perm[-6:-3]) % 7 != 0):
        return False

    if (int(perm[-7:-4]) % 5 != 0):
        return False

    if (int(perm[-8:-5]) % 3 != 0):
        return False

    if (int(perm[-9:-6]) % 2 != 0):
        return False

    return True

# print(sum(filter(isValid,map(lambda x:int(''.join(x)), perms))))

sumNums = 0
for perm in perms:
    current = ''.join(perm)
    if (isValid(current)):
        sumNums += int(current)

print(sumNums)
endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
