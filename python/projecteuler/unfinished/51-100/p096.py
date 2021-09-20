"""
 https://projecteuler.net/problem=96
 Su Doku

 Su Doku (Japanese meaning number place ) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid. 
 
 
 0 0 3 9 0 0 0 0 1 
 0 2 0 3 0 5 8 0 6 
 6 0 0 0 0 1 4 0 0 
 0 0 8 7 0 0 0 0 6 
 1 0 2 0 0 0 7 0 8 
 9 0 0 0 0 8 2 0 0 
 0 0 2 8 0 0 0 0 5 
 6 0 9 2 0 3 0 1 0 
 5 0 0 0 0 9 3 0 0 
 
 
 
 4 8 3 9 6 7 2 5 1 
 9 2 1 3 4 5 8 7 6 
 6 5 7 8 2 1 4 9 3 
 5 4 8 7 2 9 1 3 6 
 1 3 2 5 6 4 7 9 8 
 9 7 6 1 3 8 2 4 5 
 3 7 2 8 1 4 6 9 5 
 6 8 9 2 5 3 4 1 7 
 5 1 4 7 6 9 3 8 2 
 
 
 A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction. 
 The 6K text file, sudoku.txt (right click and \'Save Link/Target As...\'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above). 
 By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
import time
import numpy as np
from  projecteuler.utils.getinput import getinput

startTime = time.perf_counter()


num_puzzles = 50
f = getinput(96)
i = 0
puzzles = []
while (i < num_puzzles):
    puzzle = []
    f.readline() #get rid of "Grid ##"
    for j in range(0,9):
        line = [int(k) for k in f.readline().strip()]
        puzzle.append(line)
    puzzles.append(puzzle)
    i += 1

def check_row(puzzle,i):
    row_set = set()
    for j in range(0,9):
        cur = puzzle[i][j]
        if cur == 0:
            continue
        if cur in row_set:
            return False
        row_set.add(cur)
    del row_set
    return True

def check_col(puzzle,j):
    col_set = set()
    for i in range(0,9):
        cur = puzzle[i][j]
        if cur == 0:
            continue
        if cur in col_set:
            return False
        col_set.add(cur)
    del col_set
    return True

def check_3x3box(puzzle,i,j):
    box_set = set()
    for x in range(i - (i%3),(i -  (i%3) + 3)):
        for y in range(j - (j%3), (j - (j%3) + 3)):
            cur = puzzle[x][y]
            if cur == 0:
                continue
            if cur in box_set:
                return False
            box_set.add(cur)
    del box_set
    return True

def place_num(puzzle,i,j,num):
    new_puzzle = [row[:] for row in puzzle]
    new_puzzle[i][j] = num
    if (check_row(new_puzzle,i) and check_col(new_puzzle,j) and check_3x3box(new_puzzle,i,j)):
        return new_puzzle
    else:
        del new_puzzle
        return False

def is_complete(puzzle):
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j] == 0:
                return False
    return True

def get_pos_cell(puzzle,i,j):
    nums = set(range(1,10))
    for x in range(0,9):
        cur = puzzle[x][j]
        if (cur and cur in nums):
            nums.remove(cur)
        cur = puzzle[i][x]
        if (cur and cur in nums):
            nums.remove(cur)
    for x in range(i - (i % 3),i - (i % 3) + 3):
        for y in range(j - (j % 3),j - (j % 3) + 3):
            #print "genset:",x,y
            cur = puzzle[x][y]
            if (cur and cur in nums):
                nums.remove(cur)
    return nums
def print_puzzle(puzzle):
    for row in puzzle:
        print(''.join([str(i) for i in row]))
def solve(puzzle):
    print("calling solve....")
    for i in range(0,9):
        for j in range(0,9):
            if (puzzle[i][j] == 0):
                nums = get_pos_cell(puzzle,i,j)
                #print i,j, nums
                if (len(nums) == 0):
                    return False
                for num in nums:
                    new_puzzle = place_num(puzzle,i,j,num)
                    if (new_puzzle):
                        #print_puzzle(new_puzzle)
                        #print ""
                        if (is_complete(new_puzzle)):
                            print_puzzle(new_puzzle)
                            endTime = time.time()
                            print("")
                            print("time elapsed:", endTime - startTime)
                            import sys
                            sys.exit(0)
                        else:
                            # print "puzzle:"
                            # print_puzzle(new_puzzle)
                            # print ""
                            solve(new_puzzle)

startTime = time.time()
solve(puzzles[0])

endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
