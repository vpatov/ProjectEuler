"""
 https://projecteuler.net/problem=74
 Digit factorial chains


 The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145: 
 1! + 4! + 5! = 1 + 24 + 120 = 145 
 Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist: 
 169 -> 363601 -> 1454 -> 169 
871 -> 45361 -> 871 
872 -> 45362 -> 872 
 It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example, 
 69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454) 
78 -> 45360 -> 871 -> 45361 (-> 871) 
540 -> 145 (-> 145) 
 Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms. 
 How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

import time
startTime = time.clock()

#precomputed factorials
facts = [1,1,2,6,24,120,720,5040,40320,362880]

def factSum(num):
    sumFact = 0
    for digit in str(num):
        sumFact += facts[int(digit)]
    return sumFact

globalChains = dict()

def lengthChain(num):
    chain = set([num])
    count = 1
    newNum = factSum(num)
    while (not chain.__contains__(newNum)):
        chain.add(newNum)
        if (globalChains.__contains__(newNum)):
            return globalChains[newNum] + count
        count += 1
        newNum = factSum(newNum)
    return count

countSixty = 0
for i in range(1,1000000):
    currentLength = lengthChain(i)
    globalChains[i] = currentLength
    if (currentLength == 60):
        countSixty += 1

print(countSixty)


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
