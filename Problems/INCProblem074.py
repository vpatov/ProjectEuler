"""
 https://projecteuler.net/problem=74
 Digit factorial chains


 The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145: 
 1! + 4! + 5! = 1 + 24 + 120 = 145 
 Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist: 
 169 \xe2\x86\x92 363601 \xe2\x86\x92 1454 \xe2\x86\x92 169 
871 \xe2\x86\x92 45361 \xe2\x86\x92 871 
872 \xe2\x86\x92 45362 \xe2\x86\x92 872 
 It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example, 
 69 \xe2\x86\x92 363600 \xe2\x86\x92 1454 \xe2\x86\x92 169 \xe2\x86\x92 363601 (\xe2\x86\x92 1454) 
78 \xe2\x86\x92 45360 \xe2\x86\x92 871 \xe2\x86\x92 45361 (\xe2\x86\x92 871) 
540 \xe2\x86\x92 145 (\xe2\x86\x92 145) 
 Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms. 
 How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
