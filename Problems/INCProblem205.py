"""
 https://projecteuler.net/problem=205
 Dice Game

 Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4. 
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6. 

 Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal. 

 What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""

import time
startTime = time.clock()




possibilities = 4**9 * 6**6
print(7009890480  / possibilities)

#probability pete beats colin equals peteWins / totalPossibilities


#peter has four three sided die
#colin has two two sided die

#same as peter having two three sided and colin one two sided???

peterWins = 0

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            for l in range(1,4):
                for m in range(1,4):
                    for n in range(1,4):
                        if (sum((i,j,k,l))) > sum((m,n)) :
                            peterWins += 1

tot = 3**4 * 3**2
print(peterWins,tot,peterWins/tot)

###
### 7009890480
###

peterWins = 0
for i in range(1,4):
    for j in range(1,4):
        for m in range(1,4):
            if (sum((i,j))) > m:
                peterWins += 1

tot = 3**2 * 3
print(peterWins,tot,peterWins/tot)

# peterWins = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             for l in range(1,7):
#                 for m in range(1,7):
#                     if (i + j + k > l + m):
#                         peterWins += 1
#
# print(peterWins)
#
# print(peterWins/possibilities)



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
