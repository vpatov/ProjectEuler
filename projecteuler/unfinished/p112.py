"""
 https://projecteuler.net/problem=112
 Bouncy numbers

 Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468. 
 Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420. 
 We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349. 
 Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538. 
 Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%. 
 Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

import time
import itertools
startTime = time.clock()

# Strategy - since the bouncy numbers are far more numerous (we are in particular interested in the number beneath which 99% of the numbers are bouncy).
# it is far better (and easier) to enumerate the non-bouncy numbers, that is, the increasing and decreasing numbers. The steps will be approximately
# as follows:
#
#   1) Pick an upper bound for the number of digits the highest number we explore will have. Let's say 8, so we're not looking past 10^7/
#   2) For each number of digits, generate all increasing numbers and decreasing numbers, and put them in a set.
#     a) To generate increasing numbers, start with '1'*(number of digits). For 3, it will be 112 (Note that 111 is not increasing or decreasing).
#        Then, 113, 114, ... 119, then 122, 123, ...  and so forth. Same logic goes for decreasing numbers. This can be done with multiple for loops,
#        but there is probably a more elegant way.
#   3) Once the non-bounch numbers are generated, take the highest number we've generated as the denominator, and the difference between that and
#      the length of the increasing/decreasing sets as the denominator to receive the ratio. It will probably not be 99%, hopefully it will be 
#      higher. If it is lower, than we have picked an upper bound that is too low. If it is higher, then we just need to find the non-bouncy numbers 
#      that are closest to that 99% boundary (if its not a non-bouncy number directly on the boundary), and then simply iterate downwards from there 



numdigits = 8
start_digit = 3


"""
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
"""

def generate_increasing():
  iter_recur(9,1,10,[])

def iter_recur(depth,start,bound,variables):
  #print("iter_recur called with {} {} {} {}".format(depth,start,bound,variables))
  if depth == 0:
    for i in range(variables[-1],bound):
      print(variables + [i])
  else:
    for i in range(variables[-1] if len(variables) != 0 else start,bound):
      iter_recur(depth-1,start,bound,variables + [i])


generate_increasing()


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
