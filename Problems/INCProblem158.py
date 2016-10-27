"""
 https://projecteuler.net/problem=158
 Exploring strings for which only one character comes lexicographically after its neighbour to the left
Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed. 
Examples are 'abc', 'hat' and 'zyx'. 
When we study these three examples we see that for 'abc' two characters come lexicographically after its neighbour to the left. 
For 'hat' there is exactly one character that comes lexicographically after its neighbour to the left. For 'zyx' there are zero characters that come lexicographically after its neighbour to the left. 
In all there are 10400 strings of length 3 for which exactly one character comes lexicographically after its neighbour to the left.
 We now consider strings of n <= 26 different characters from the alphabet.
For every n , p( n ) is the number of strings of length n for which exactly one character comes lexicographically after its neighbour to the left. 
 What is the maximum value of p( n )?
"""

import time
startTime = time.clock()

def string_islex(input):
    one = False
    for i in range(0,len(input) - 1):
        if input[i] < input[i+1]:
            if not one:
                one = True
            else:
                return False
    return one

def build_string(args):
    return ''.join([chr(x + ord('a')) for x in args])

from itertools import product
from fractions import Fraction


len_alphabet = 11
for r in range(1,len_alphabet):
    count_elig = 0
    count_all = 0

    for items in product(range(0,len_alphabet),repeat=r):
        indeces = set(items)
        if (len(indeces) != len(items)):
            continue
        string = build_string(list(item for item in items))
        if (string_islex(string)):
            count_elig += 1
        count_all += 1

    print count_elig
    print count_all
    ratio = Fraction(count_elig,count_all)
    print ratio
    print '\n'



endTime = time.clock()
print "Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds."
