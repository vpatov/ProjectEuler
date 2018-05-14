"""
 https://projecteuler.net/problem=345
 Matrix Sum

 We define the Matrix Sum of a matrix as the maximum sum of matrix elements with each element being the only one in his row and column. For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767): 

 
\xc2\xa0\xc2\xa07 \xc2\xa053 183 439 863 
497 383 563 \xc2\xa079 973 
287 \xc2\xa063 343 169 583 
627 343 773 959 943 767 473 103 699 303 

 
Find the Matrix Sum of: 
 
\xc2\xa0\xc2\xa07 \xc2\xa053 183 439 863 497 383 563 \xc2\xa079 973 287 \xc2\xa063 343 169 583 
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913 
447 283 463 \xc2\xa029 \xc2\xa023 487 463 993 119 883 327 493 423 159 743 
217 623 \xc2\xa0\xc2\xa03 399 853 407 103 983 \xc2\xa089 463 290 516 212 462 350 
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350 
870 456 192 162 593 473 915 \xc2\xa045 989 873 823 965 425 329 803 
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326 
322 148 972 962 286 255 941 541 265 323 925 281 601 \xc2\xa095 973 
445 721 \xc2\xa011 525 473 \xc2\xa065 511 164 138 672 \xc2\xa018 428 154 448 848 
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198 
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390 
821 461 843 513 \xc2\xa017 901 711 993 293 157 274 \xc2\xa094 192 156 574 
\xc2\xa034 124 \xc2\xa0\xc2\xa04 878 450 476 712 914 838 669 875 299 823 329 699 
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107 
813 883 451 509 615 \xc2\xa077 281 613 459 205 380 274 302 \xc2\xa035 805
"""
import time
import itertools
import random
import numpy as np
from projecteuler.utils.getinput import getinput
startTime = time.clock()

# Good old fashioned constraint optimization problem
# Seems like a good fit for the minimum conflicts heuristic
# Update - ended up using a stochastic solution! :)


f = getinput(345)
matrix = [[int(num) for num in line.split()] for line in f.readlines()]



# Use a small enough submatrix such that brute forcing is possible, to allow for ground truth source
test_length = 9
test_matrix = [line[:test_length] for line in matrix[:test_length]]

# If we want to try all 15! combinations, it would probably take much more than a minute :)
# Thought process: using something similar to a min-conflicts approach do this: Starting with each column,
# take the largest element and consider it part of the sum. Move on to the next column, and take the largest
# element that doesn't conflict with the previous choice (can't be in the same row as previous choices). Do this
# until you reach the end of the matrix. Calculate the sum, store. For every column, see if that column's choice
# can be switched with any other column's choice to create a larger sum. If so, perform the switch. Keep doing this
# until no switches are possible. Hopefully this results in the correct answer. Anyway, whatever methodology you choose,
# test it extensively on a small subset, for which you are able to completely and correctly verify the correct answer 
# via brute-force.

# Assume matrix is square to make life easier


def brute_force(matrix):
  max_sum = 0
  max_cells = None
  for combo in itertools.permutations(range(len(matrix))):
    current_sum = 0
    for row,col in zip(range(len(matrix)),combo):
      current_sum += matrix[row][col]
    if current_sum > max_sum:
      max_sum = current_sum
      max_cells = combo
  return max_sum,max_cells



# Deprecated
def initialize_choice(matrix):
  """
    Deprecated in favor of random_init, which allows for a stochastic solution strategy
  """
  lookup = {}
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      if matrix[row][col] in lookup:
        lookup[matrix[row][col]].append((row,col))
      else:
        lookup[matrix[row][col]] = [(row,col)]
 
  # flatten the matrix into an array 
  flatnums = sorted(list(np.ndarray.flatten(np.array(matrix))),reverse=True)

  chosen_rows = set()
  chosen_cols = set()
  chosen_nums = []
  for i in range(0,len(flatnums)):
    row,col = lookup[flatnums[i]][0]
    if row in chosen_rows or col in chosen_cols:
      continue
    else:
      chosen_rows.add(row)
      chosen_cols.add(col)
      chosen_nums.append((row,col,matrix[row][col]))

  return chosen_nums



def random_init(matrix):
  """
    Randomly initialize the number choices for the sum.
  """
  chosen_nums = []
  available_rows = list(range(len(matrix)))
  available_cols = list(range(len(matrix)))
  while(len(chosen_nums) != len(matrix)):
      row = random.sample(available_rows,1)[0]
      col = random.sample(available_cols,1)[0]
      available_rows.remove(row)
      available_cols.remove(col)
      chosen_nums.append((row,col,matrix[row][col]))

  return chosen_nums



def iter_solve(matrix,chosen_nums):
  """
    Iterate over the chosen numbers and matrix, and make number switches that increase the sum.
    For some initializations, this algorithm converges at a local maxima. However, the algorithm
    is very fast, so it is very easy to try around 1k initializations, and for the purposes of 
    the projecteuler problem, this got me the answer (I think maybe even 50 is enough, but since
    its so fast might as well do 1k).
  """

  current_sum = sum([num for r,c,num in chosen_nums])

  # Find the smallest number that is part of the chosen nums, and see all the switches that it can make,
  # in its own column. Make the switch that adds the most to the sum. Repeat process until there are no
  # switches that would add to the sum. Theoretically, this should work from any initilization - would be
  # good to test that to be sure. 

  # Idea -- If, after correct implementation of the propoed methodology, the algorithm does not manage
  # to converge to the right answer in some cases, then the algorithm can be bolstered by a stochastic
  # approach. Try random initializations and keep track of the maximum sum the algorithm converges to
  # given that initialization. UPDATE: Implemented, idea works. :)

  # Note -- If implemented correctly this algorithm is guaranteed to converge (possibly at a local maxima)
  # because it will only switch if the sum increases, so it won't have the chance to get caught in any search loops.

  min_nums = sorted(chosen_nums,key=lambda x: x[2])
  
  for min_row,min_col,min_num in min_nums:

    max_sum = current_sum
    swap1, swap2 = None,None

    for row in range(0,len(matrix)):
      if row == min_row:
        continue

      # calculate the sum that would happen if we made the switch, and see if its better
      # keep track of the coordinates of the switch (so we can make it later if need be)
      # we should be able to lookup chosen numbers by rows and by columns. Extra
      # data structures would make every lookup easier but the tradeoff is that it 
      # will become more complex to maintain the data structures. I'm sure an elegant
      # choice is lurking about somewhere...

      # Naming these variables in a non-confusing manner is a bit difficult right now...
      # Draw out a diagram to show what is happening with the variables

      """
      ----------------------------------------
      X    X    min_num          X   new_num
      X    X    X                X   X
      X    X    candidate_num    X   old_num
      X    X    X                X   X
      ---------------------------------------

      min_num - number in matrix (not necessarily the smallest, although we do start iterating from the smallest)
      candidate_num - number in the same column as the min_num, that if switched with min_num (and old_num and
      new_num are switched), adds the most to the sum than if any other switches in min_num's column were made.
      old_num - current chosen number in same row as candidate, that would get switched with candidate row-wise and
      switched with new_num column wise (remember, only one number per row and per column)
      new_num - new number in same row as min_num, and same column as old_num.

      """

      # iterate over the current candidate
      # find the numbers that would also be switched as a result of switching
      # the current candidate number
      candidate_num = matrix[row][min_col]
      for r,c,m in chosen_nums:
        if r == row:
          old_row,old_col,old_num = r,c,matrix[r][c]
          new_row,new_col,new_num = min_row,c,matrix[min_row][c]
          break

      # Calculate potential sum if switch was made
      placeholder_sum = current_sum
      placeholder_sum -= min_num
      placeholder_sum += candidate_num
      placeholder_sum -= old_num
      placeholder_sum += new_num


      # If sum is greater than current maximum, keep track of switch to be made
      if placeholder_sum > max_sum:
        max_sum = placeholder_sum
        swap1 = ((min_row,min_col,min_num),(row,min_col,candidate_num))
        swap2 = ((old_row,old_col,old_num),(new_row,new_col,new_num))      


      # continue statement added for whitespace clarity      
      continue


    # If we found a switch that increases the sum, make it
    if swap1 != None:
      chosen_nums.remove(swap1[0])
      chosen_nums.append(swap1[1])
      chosen_nums.remove(swap2[0])
      chosen_nums.append(swap2[1])
      current_sum = sum([num for r,c,num in chosen_nums])
      return chosen_nums

    # If we haven't found a switch, return False, means that the algorithm
    # has converged at its current initialization
    else:
      return False



# Don't try to brute force any matrix greater than size 10.
# For 11 it takes around a minute, for 12 around 10 minutes, so forth..
# ground_truth = brute_force(matrix)
# print("Ground Truth:",ground_truth)



# Iterate over stochastic initializations, and after 1000, pick the best one, and consider that
# the answer. If the fate of the world depended on this algorithm solving this for something like matrix size 1000, 
# I wouldn't bet on that, but for size 15 with infinite retries on project euler (even though it worked on first try), 
# is good enough for me.

max_sum = 0
for iteration in range(1000):
  
  chosen_nums = random_init(matrix)
  chosen_sum = 0
  while(True):
    result = iter_solve(matrix,chosen_nums)
    if not result:
      break  
    chosen_nums = result
    chosen_sum = sum([num for r,c,num in chosen_nums])
  
  if chosen_sum > max_sum:
    max_sum = chosen_sum

print(max_sum)









endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
