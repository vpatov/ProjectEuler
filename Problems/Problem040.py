"""
 https://projecteuler.net/problem=40
 Champernowne\'s constant

 An irrational decimal fraction is created by concatenating the positive integers: 
 0.12345678910 1 112131415161718192021... 
 It can be seen that the 12^th digit of the fractional part is 1. 
 If d _ n represents the n ^th digit of the fractional part, find the value of the following expression. 
 d _1 * d _10 * d _100 * d _1000 * d _10000 * d _100000 * d _1000000
"""

import time
startTime = time.clock()

sequence = ['1'] * 1000500
length = 0
i = 1
while (length < 1000000):
    num = str(i)
    for digit in num:
        sequence[length] = digit
        length += 1
    i += 1

print(int(sequence[0]) * int(sequence[9]) * int(sequence[99]) * int(sequence[999]) *
      int(sequence[9999]) * int(sequence[99999]) * int(sequence[999999]))



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
