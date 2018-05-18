"""
 https://projecteuler.net/problem=93
 Arithmetic expressions

 By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, -, *, /) and brackets/parentheses, it is possible to form different positive integer targets. 
 For example, 
 8 = (4 * (1 + 3)) / 2 
14 = 4 * (3 + 1 / 2) 
19 = 4 * (2 + 3) - 1 
36 = 3 * 4 * (2 + 1) 
 Note that concatenations of the digits, like 12 + 34, are not allowed. 
 Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number. 
 Find the set of four distinct digits, a &lt; b &lt; c &lt; d , for which the longest set of consecutive positive integers, 1 to n , can be obtained, giving your answer as a string: abcd .
"""
import time
import itertools
import numpy as np
import cProfile

startTime = time.clock()

# This problem obviously begs for the use of postfix notation.
# Considering that we can only use four digits, and that a < b < c < d, there 
# are not that many combinations to iterate through


# infix                   postfix
# 2 + 3                   2 3 +
# (5 - 7) * 2             5 7 - 2 *

digits = '0123456789'
ops = {
  '+': lambda x,y: x + y,
  '-': lambda x,y: x - y,
  '*': lambda x,y: x * y,
  '/': lambda x,y: x / y if y != 0 else None
}

def postfix_eval(expression):
  index = 0
  stack_index = 0
  stack = [0] * 8
  while(index < len(expression)):
    char = expression[index]
    if char in range(0,10):
      stack[stack_index] = char
      stack_index += 1
    else:
      stack_index -= 2
      if stack_index < 0:
        return None
      y,x = stack[stack_index],stack[stack_index+1]
      res = ops[char](x,y)
      if res == None:
        return None
      stack[stack_index] = res
      stack_index += 1
    index += 1
  if stack_index == 1:
    return stack[0]
  else:
    return None

limit = 9*8*7*6 + 1





def main():
  longest_set = 0
  longest_numbers = None
  longest_results = None

  for d in range(1,10):
    for c in range(d+1,10):
      for b in range(c+1,10):
        for a in range(b+1,10):
          print(a,b,c,d)
          operator_combinations = itertools.product(*['*/-+']*3)
          results = np.zeros(limit)
          for combo in operator_combinations:
            expressions = itertools.permutations((a,b,c,d,*combo),7)
            for expression in expressions:
              res = postfix_eval(expression)
              if res != None and res % 1 == 0 and res > 0:
                results[int(res)] = 1

          for i in range(1,limit):
            if not results[i]:
              if i > longest_set:      
                longest_set = i
                longest_numbers = a,b,c,d
                longest_results = results
                break
              else:
                break
  return longest_set, longest_numbers, longest_results

import sys
prof = cProfile.Profile()
retval = prof.runcall(main)

longest_set, longest_numbers, longest_results = retval

prof.print_stats()


endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
