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
import numpy as np
from projecteuler.utils.getinput import getinput
startTime = time.clock()

# Good old fashioned constraint optimization problem
# Seems like a good fit for the minimum conflicts heuristic



f = getinput(345)
matrix = [[int(num) for num in line.split()] for line in f.readlines()]


test_sum = 3315
test_input = """  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303"""
test_matrix = [[int(num) for num in line.split()] for line in test_input.split('\n')]


matrix = test_matrix
# test_length = 8
# matrix = [line[:test_length] for line in matrix[:test_length]]
# matrix = test_matrix

# If we want to try all 15! combinations, it would probably take much more than a minute :)
# Thought process: using something similar to a min-conflicts approach do this: Starting with each column,
# take the largest element and consider it part of the sum. Move on to the next column, and take the largest
# element that doesn't conflict with the previous choice (can't be in the same row as previous choices). Do this
# until you reach the end of the matrix. Calculate the sum, store. For every column, see if that column's choice
# can be switched with any other column's choice to create a larger sum. If so, perform the switch. Keep doing this
# until no switches are possible. Hopefully this results in the correct answer. Anyway, whatever methodoloy you choose,
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


def initialize_choice(matrix):
	lookup = {}
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] in lookup:
				lookup[matrix[row][col]].append((row,col))
			else:
				lookup[matrix[row][col]] = [(row,col)]
	
	print(lookup)
	flatnums = sorted(list(np.ndarray.flatten(np.array(matrix))),reverse=True)
	print(flatnums)

	for key in lookup:
		if len(lookup[key]) > 1:
			print(key, lookup[key])

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



	# for i in range(0,len(chosen_rows)):
	# 	print(matrix[chosen_rows[i]][chosen_cols[i]])

	current_sum = sum([num for r,c,num in chosen_nums])
	print(current_sum, chosen_nums)

	# Find the smallest number that is part of the chosen nums, and see all the switches that it can make,
	# in its own column. Make the switch that adds the most to the sum. Repeat process until there are no
	# switches that would add to the sum. Theoretically, this should work from any initilization - would be
	# good to test that to be sure. 

	# Idea -- If, after correct implementation of the propoed methodology, the algorithm does not manage
	# to converge to the right answer in some cases, then the algorithm can be bolstered by a stochastic
	# approach. Try random initializations and keep track of the maximum sum the algorithm converges to
	# given that initialization. 

	# Note -- If implemented correctly this algorithm is guaranteed to converge because it will only 
	# switch if the sum increases, so it won't have the chance to get caught in any search loops.

	min_row,min_col,min_num = min(chosen_nums,key=lambda x: x[2])
	max_sum = current_sum

	for row in range(0,len(matrix)):
		if row == min_row:
			continue

		# calculate the sum that would happen if we made the switch, and see if its better
		# keep track of the coors of the switch (so we can make it later if need be)
		# we should be able to lookup chosen numbers by rows and by columns. Extra
		# data structures would make every lookup easier but the tradeoff is that it 
		# will become more complex to maintain the data structures. I'm sure an elegant
		# choice is lurking about somewhere...

		# Naming these variables in a non-confusing manner is a bit difficult right now...
		# Draw out a diagram to show what is happening with the variables


		candidate_num = matrix[row][min_col]
		for r,c,m in chosen_nums:
			if r == row:
				old = matrix[r][c]
				new = matrix[min_row][c]
				break

		print("Candidate_num: ", candidate_num)
		print("old:", old, "new:", new)


		placeholder_sum = current_sum
		placeholder_sum -= min_num
		placeholder_sum += candidate_num
		placeholder_sum -= old
		placeholder_sum += new

		print(placeholder_sum) # So far this is correct!!

		## MAKE THE SWITCH









initialize_choice(matrix)








endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
