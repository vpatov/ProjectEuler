"""
 https://projecteuler.net/problem=34
 Digit factorials


 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. 
 Find the sum of all numbers which are equal to the sum of the factorial of their digits. 
 Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import time
startTime = time.clock()

facts = [1,1] + ([1] * 8)
for i in range(2,10):
    facts[i] *= facts[i-1] * i

def isSumFactsOfDigits(n):
    num = str(n)
    sum = 0
    for digit in num:
        sum += facts[int(digit)]
    return sum == n

# I love writing these pretty one-liners when I can :)
print(sum(filter(isSumFactsOfDigits,range(10,facts[9]))))

# #### An easy to understand, multi-line alternative
# #### facts[9] = 9! is an upperbound for where we need to look
# sumNums = 0
# for i in range(10,facts[9]):
#     if (isSumFactsOfDigits(i)):
#         sumNums += i
# print(sumNums)

endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
