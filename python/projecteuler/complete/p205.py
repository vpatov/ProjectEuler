"""
 https://projecteuler.net/problem=205
 Dice Game

 Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4. 
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6. 

 Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal. 

 What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""
import time
import numpy as np
import itertools
import colorama
from functools import reduce
from fractions import Fraction
from operator import mul
startTime = time.perf_counter()



def nCk(n,k): 
  return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))
  
def c(p,n,s):
  summ = 0
  for k in range(0,int((p-n)/s)+1):
    summ += (-1)**k * nCk(n,k) * nCk(p  - (s*k) - 1, n - 1)
  return summ




def problem_205(n1,s1,n2,s2):
  pete, collin = [0]*(s1*n1 + 1), [0]*(s2*n2 + 1)

  for roll in range(1*n1,s1*n1 + 1):
    pete[roll] = c(roll,n1,s1)

  for roll in range(1*n2,s2*n2 + 1):
    collin[roll] = c(roll,n2,s2)

  psums, csums = [0]*(s1*n1 + 1),[0]*(s2*n2 + 1)
  psums[1*n1] = sum(pete)
  csums[1*n2] = sum(collin)
  for i in range(1*n1 + 1,s1*n1 + 1):
    psums[i] = psums[i-1] - pete[i-1]

  for i in range(1*n2 + 1,s2*n2 + 1):
    csums[i] = csums[i-1] - collin[i-1]



  pete_wins = 0
  for collin_roll in range(1*n2,s2*n2 + 1):
    for pete_roll in range(1*n1,s1*n1 + 1):
      if pete_roll > collin_roll:
        pete_wins += pete[pete_roll]*collin[collin_roll]

  total_possibilities = s1**n1 * s2**n2
  print(pete_wins)
  print('{:.7f}'.format(pete_wins/total_possibilities))
      

n1,s1 = 9,4
n2,s2 = 6,6
problem_205(n1,s1,n2,s2)



# brute force testing
"""
p_wins = 0
total = 4**2 * 6**3
count_tot = 0
break_colin = False
for p1 in range(1,s1+1):
  for p2 in range(1,s1+1):
    for c1 in range(1,s2+1):
      for c2 in range(1,s2+1):
        for c3 in range(1,s2+1):
 
          count_tot += 1
          p_tot = p1 + p2 
          c_tot = c1 + c2 + c3

          p,c = (p1,p2),(c1,c2,c3)

          if p_tot == c_tot:
            #print(colorama.Fore.BLUE + str((p,c)) + colorama.Fore.RESET, end=' '*5)
            #break
            pass

          elif p_tot < c_tot:
            #print(colorama.Fore.RED + str((p,c)) + colorama.Fore.RESET, end=' '*5)
            #break
            pass
          else:
            p_wins += 1
            #print(colorama.Fore.GREEN + str((p,c)) + colorama.Fore.RESET, end=' '*5)

        #print()
print(p_wins,total)
"""
endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
