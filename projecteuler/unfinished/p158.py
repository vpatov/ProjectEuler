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
import itertools
from itertools import permutations as permute
from scipy.misc import comb
import zipfile



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

# def build_string(args):
#     return ''.join([chr(x + ord('a')) for x in args])
#
# from itertools import product
# from fractions import Fraction
#
#
# len_alphabet = 11
# for r in range(1,len_alphabet):
#     count_elig = 0
#     count_all = 0
#
#     for items in product(range(0,len_alphabet),repeat=r):
#         indeces = set(items)
#         if (len(indeces) != len(items)):
#             continue
#         string = build_string(list(item for item in items))
#         if (string_islex(string)):
#             count_elig += 1
#         count_all += 1
#
#     print count_elig
#     print count_all
#     ratio = Fraction(count_elig,count_all)
#     print ratio
#     print '\n'

# memoized_p = {2:1,1:0}
#
# def p(n):
#     if (memoized_p.has_key(n)):
#         return memoized_p[n]
#     total = 0
#     for i in range(0,n-1):
#         total += 2 ** i
#     total += p(n-1)
#     memoized_p[n] = total
#     return total
#
# ps = []
# for i in range(1,27):
#     print p(i)




# perms = permute(list('abcdefghijklmnopqrstuvwxyz'),r=2)
#
#
# totalCount = 0
# count = 0
#
# firstLetter = 'a'
# secondLetter = 'b'
# for perm in perms:
#     x = ''.join(perm)
#     if (string_islex(x)):
#         if (x[0] != firstLetter):
#             print firstLetter, count
#             firstLetter = x[0]
#             count = 0
#         # if (x[1] != secondLetter):
#         #     #print firstLetter + secondLetter, count
#         #     secondLetter = x[1]
#         #     firstLetter = x[0]
#         #     count = 0
#         count+=1
#         totalCount +=1
# print firstLetter, count
# print totalCount


class diff():
    def __init__(self):
        self.diff = None
        self.value = 0

    def update(self):
        if self.diff == None:
            return self.value
        else:
            ret = self.value
            if (type(self.diff) == int):
                self.value += self.diff
            else:
                self.value += self.diff.update()
            return ret

    def __repr__(self):
        return '(' + str(self.value) + ', ' + str(self.diff) + ')'


lastStart = 0
lastDiff = 1

for n in range(2,5):
    start = int(comb(25,n-1))
    print "length:", n, '\t', "start:", start

    curSum = 0

    maindiff = diff()
    curdiff = maindiff
    curdiff.value = lastStart - lastDiff
    print "curdiff.value =", lastStart, '-', lastDiff
    for i in range(0,n-2):
        newdiff = diff()
        curdiff.diff = newdiff
        newdiff.value = lastDiff

    print "Beginning iteration for length:", n
    val = start
    for i in range(0,26):
        print val
        curSum += val
        val += maindiff.update()
    print "sum:", curSum, '\n'

    lastStart = start
    lastDiff = curdiff.value + 1




# first = diff()
# second = diff()
# third = diff()
# fourth = diff()
#
#
# first.diff = second
# first.value = 2024
#
# second.diff = third
# second.value = 253
#
# third.diff = fourth
# third.value = 22-4
#
#
#
# start = 12650
#
# print "TEST"
# totSum = 0
# for i in range(0,26):
#     print start
#     totSum += start
#     start += first.update()
#
#
# print totSum




endTime = time.clock()
print "Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds."
