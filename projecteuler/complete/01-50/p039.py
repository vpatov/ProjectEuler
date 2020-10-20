"""
 https://projecteuler.net/problem=39
 Integer right triangles

 If p is the perimeter of a right angle triangle with integral length sides, { a , b , c }, there are exactly three solutions for p = 120. 
 {20,48,52}, {24,45,51}, {30,40,50} 
 For which value of p <= 1000, is the number of solutions maximised?
"""


# This isn't a very efficient solution, but considering how quickly I wrote it, it brought me the answer
# faster than a more efficient version would :)


import time
startTime = time.perf_counter()
from math import sqrt

squares = list(i**2 for i in range(0,1000))
squareSet = set(squares)

# def getSquareIndex(p):
#     for i in range(0,len(squares)):
#         if (squares[i] > p):
#             return i-1

def solutions(p):
    start = p
    solutions = set()
    while (start > 0):
        i = start-2
        c2 = squares[i]
        i -= 1
        while (i > 2):
            if (squareSet.__contains__(c2 - squares[i])):
                if (int(sqrt(c2)) + int(sqrt(squares[i])) + int(sqrt(c2 - squares[i])) == p):
                    ans = [int(sqrt(c2)), int(sqrt(squares[i])),int(sqrt(c2 - squares[i]))]
                    ans.sort()
                    ans = tuple(ans)
                    solutions.add(ans)
            i -= 1


        start -= 1
    return solutions


maxSol = 0
maxP = 0
for p in range(1,1000):
    sols = solutions(p)
    if (len(sols) > maxSol):
        maxSol = len(sols)
        maxP = p

print(maxP)


#code


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
