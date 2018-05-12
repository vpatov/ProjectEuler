"""
It seems that prime number generation is a frequently reoccurring subtask when solving Project Euler problems...
I've been using the Sieve of Erastosthenes, which is relatively efficient O(N * log (log N)), but I just read that the Sieve of Atkin
can perform faster, in O(N) time. So I'm going to take the algorithm from the wikipedia page -

     "https://en.wikipedia.org/wiki/Sieve_of_Atkin"

and attempt to implement it here, in Python.


"""
#
#
# # The algorithm:
# # 1. Create a results list, filled with 2, 3, and 5.
# # 2. Create a sieve list with an entry for each positive integer; all entries of this list should initially be marked non prime (composite).
# # 3. For each entry number n in the sieve list, with modulo-sixty remainder r :
# # 	1.If r is 1, 13, 17, 29, 37, 41, 49, or 53, flip the entry for each possible solution to 4x^2 + y^2 = n.
# # 	2. If r is 7, 19, 31, or 43, flip the entry for each possible solution to 3x^2 + y^2 = n.
# # 	3. If r is 11, 23, 47, or 59, flip the entry for each possible solution to 3x^2 − y^2 = n when x > y.
# # 	4.If r is something else, ignore it completely.
# #
# #
# # 4. Start with the lowest number in the sieve list.
# # 5. Take the next number in the sieve list still marked prime.
# # 6. Include the number in the results list.
# # 7. Square the number and mark all multiples of that square as non prime. Note that the multiples that can be
# #   factored by 2, 3, or 5 need not be marked, as these will be ignored in the final enumeration of primes.
# # 8. Repeat steps four through seven.
#
#
#
#
#
# limit = 1000
# results = [2,3,5]
# #False means i is composite, True means i is prime, for entry sieveList[i]
# sieveList = [False] * limit
#
# squareList = list(i**2 for i in range(0,limit))
# squareDict = dict()
# for i in range(0,len(squareList)):
#     squareDict[squareList[i]] = i
#
# firstSet = set([1,13,17,29,37,41,49,53])
# secondSet = set([7,19,31,43])
# thirdSet = set([11,23,47,59])
#
#
#
# def solveFirst(n):
#     # integer solutions for 4x^2 + y^2 = n
#     # n - 4x^2 = y^2
#     sols = set()
#     i = 1
#     term = n - 4*squareList[i]
#     while (term < n and term > 0):
#
#         if squareDict.__contains__(term):
#             sols.add(i)
#             sols.add(squareDict[term])
#
#         #update
#         i += 1
#         term = n - 4*squareList[i]
#
#     return sols
#
# def solveSecond(n):
#     # integer solutions for 3x^2 + y^2 = n
#     # n - 3x^2 = y^2
#     sols = set()
#     i = 1
#     term = n - 3*squareList[i]
#     while (term < n and term > 0):
#
#         if squareDict.__contains__(term):
#             sols.add(i)
#             sols.add(squareDict[term])
#
#         #update
#         i += 1
#         term = n - 3*squareList[i]
#
#     return sols
#
# def solveThird(n):
#     # integer solutions for 3x^2 − y^2 = n when x > y.
#     # 3x^2 - n = y^2
#     sols = set()
#     i = 1
#
#     term = 3*squareList[i] - n
#     while (term < n and term > 0):
#
#         if squareDict.__contains__(term):
#             if (i > squareDict[term]):
#                 sols.add(i)
#                 sols.add(squareDict[term])
#
#         #update
#         i += 1
#         term = n - 3*squareList[i]
#
#     return sols
#
#
#
#
#
# for n in range(1,limit):
#     r = n % 60
#     if (firstSet.__contains__(r)):
#         firstSols = solveFirst(n)
#         for sol in firstSols:
#             sieveList[sol] = not sieveList[sol]
#
#     elif (secondSet.__contains__(r)):
#         secondSols = solveSecond(n)
#         for sol in secondSols:
#             sieveList[sol] = not sieveList[sol]
#
#     elif (thirdSet.__contains__(r)):
#         thirdSols = solveThird(n)
#         for sol in thirdSols:
#             sieveList[sol] = not sieveList[sol]
#
#
# # 4. Start with the lowest number in the sieve list.
# # 5. Take the next number in the sieve list still marked prime.
# # 6. Include the number in the results list.
# # 7. Square the number and mark all multiples of that square as non prime. Note that the multiples that can be
# #   factored by 2, 3, or 5 need not be marked, as these will be ignored in the final enumeration of primes.
# # 8. Repeat steps four through seven.
#
# i = 0
# while (i < len(sieveList)):
#     if (sieveList[i]):
#         results.append(i)
#         multiple = i ** 2
#         base = multiple
#         while (multiple < limit):
#             sieveList[multiple] = False
#             multiple += base
#     i += 1
#
# print(results)




import math
import time
import sys
import json
import os
import numpy as np

def sieve_atkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

def sieve_atkin_nump(limit):
  pass 


if __name__ == '__main__':
  startTime = time.clock()
  
  limit = int(sys.argv[1])  

  if len(sys.argv) == 3:
    target_dir = sys.argv[2]
  else:
    target_dir = '.'

  primes = sieve_atkin(limit)
  filename = 'primes_up_to_' + str(limit) + '.json'

  with open(os.path.join(target_dir,filename),'w') as f:
    json.dump(primes,f)
  endTime = time.clock()
  print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")




