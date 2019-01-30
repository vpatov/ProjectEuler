"""
 https://projecteuler.net/problem=61
 Cyclical figurate numbers

 Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae: 
 Triangle 
 \xc2\xa0 
 P_3, n = n ( n +1)/2 
 \xc2\xa0 
 1, 3, 6, 10, 15, ... 
 Square 
 \xc2\xa0 
 P_4, n = n ^2 
 \xc2\xa0 
 1, 4, 9, 16, 25, ... 
 Pentagonal 
 \xc2\xa0 
 P_5, n = n (3 n -1)/2 
 \xc2\xa0 
 1, 5, 12, 22, 35, ... 
 Hexagonal 
 \xc2\xa0 
 P_6, n = n (2 n -1) 
 \xc2\xa0 
 1, 6, 15, 28, 45, ... 
 Heptagonal 
 \xc2\xa0 
 P_7, n = n (5 n -3)/2 
 \xc2\xa0 
 1, 7, 18, 34, 55, ... 
 Octagonal 
 \xc2\xa0 
 P_8, n = n (3 n -2) 
 \xc2\xa0 
 1, 8, 21, 40, 65, ... 
 The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties. 
 The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first). 
 Each polygonal type: triangle (P_3,127 =8128), square (P_4,91 =8281), and pentagonal (P_5,44 =2882), is represented by a different number in the set. 
 This is the only set of 4-digit numbers with this property. 
 Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""


import time
from collections import defaultdict
startTime = time.perf_counter()


# Plan:
# 1) Generate all figurate numbers for n in 3,4,5,6,7,8
# 2) Only for the 4-digit figurate numbers, create dicts for each two digit start combination and end combination. 
#   i.e., 8281 will be an entry in start_set[82] and in end_set [81]
# 3) For each number, Perform a breadth first search for cyclical chains, and memoize the lengths and sums of each chain. Explore
#     longest chains first (obv).
# Since the problem says "the only set", rest assured there is only one, and terminate once found.


# Okay, how to reason about the search? The naive method of searching for cycles goes too wild too quick 

figurate_numbers = {}
for i in range(3,9):
  cur = 1
  base_addend = i - 2
  cur_addend = i - 1
  nums = [cur]
  while (cur < 10_000):
    cur += cur_addend
    nums.append(cur)
    cur_addend += base_addend

  figurate_numbers[i] = nums

for order in figurate_numbers:
  figurate_numbers[order] = set([str(num) for num in filter(lambda x: x >= 1000 and x <= 9999, figurate_numbers[order])])


def memberof(num):
  return tuple([order for order in figurate_numbers if num in figurate_numbers[order]])

start_set = defaultdict(list)
end_set = defaultdict(list)
for order in figurate_numbers:
  for strnum in figurate_numbers[order]:
    start,end = strnum[:2],strnum[2:]
    start_set[start].append((strnum,memberof(strnum)))
    end_set[end].append((strnum,memberof(strnum)))


def find_cycles(first,num,cycle,cycles):
  start,end = num[:2],num[2:]
  if end in start_set:
    for term,members in start_set[end]:
      if term[:2] == first:
        cycles.append(cycle)
      if term not in cycle:
        if len(cycle) != 6:
          find_cycles(first,term,cycle+[term],cycles)


all_cycles = {}
for order in figurate_numbers:
  for number in figurate_numbers[order]:
    if number not in all_cycles:
      cur_cycles = []
      find_cycles(number[:2],number,[number],cur_cycles)
      all_cycles[number] = cur_cycles


for number in all_cycles:
  all_cycles[number] = [cycle for cycle in all_cycles[number] if len(cycle) == 6]


def satisfies(cycle):
  singles = list(filter(lambda x: len(x) == 1,[memberof(term) for term in cycle]))
  if len(set(singles)) != len(singles):
    return False 
  cyclemembers = set([memberof(term) for term in cycle])
  return len(cyclemembers) == 6

breakout = False
for number in all_cycles:
  if breakout:
    break
  for cycle in all_cycles[number]: 
    if satisfies(cycle):
      print(sum([int(i) for i in cycle]))
      breakout = True
      break



endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")








