"""
 https://projecteuler.net/problem=62
 Cubic permutations

 The cube, 41063625 (345^3 ), can be permuted to produce two other cubes:
 56623104 (384^3 ) and 66430125 (405^3 ). In fact, 41063625 is the smallest cube which has exactly
 three permutations of its digits which are also cube.
 Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import time
startTime = time.perf_counter()


# First Attempt : Runs in about 50 seconds, and is slower than I'd like.
#
# upperBound = 11000
# cubeList = list(i**3 for i in range(0,upperBound))
# cubeSet = set(cubeList)
#
# def isPerm(number1, number2):
#     num1 = list(str(number1))
#     num2 = list(str(number2))
#     num1.sort()
#     num2.sort()
#     return num1 == num2
# i = 0
# found = False
# while(True and not found and i < 11000):
#     count = 1
#     currentCube = cubeList[i]
#     nextIndex = 1
#     nextCube = cubeList[i+nextIndex]
#     while(len(str(currentCube)) == len(str(nextCube))):
#         if isPerm(currentCube,nextCube):
#             count += 1
#         if (count == 5):
#             print(currentCube)
#             found = True
#             break
#         nextIndex += 1
#
#         if (nextIndex + i >= len(cubeList)):
#             print("upperBound of" , upperBound , "is too low")
#             found = True
#             break
#
#         nextCube = cubeList[i+nextIndex]
#
#
#     i += 1


# Second Attempt - much much much faster! I realized I could just sort the digits, and use a dictioanry to keep track of them.
upperBound = 11000
cubeList = list(''.join(sorted(str(i**3))) for i in range(0,upperBound))
cubeDict = dict()


for i in range(0,len(cubeList)):
    if cubeDict.__contains__(cubeList[i]):
        cubeDict[cubeList[i]][0] += 1
        if (cubeDict[cubeList[i]][0]) == 5:
            print(int(cubeDict[cubeList[i]][1]) ** 3)
            break
    else:
        cubeDict[cubeList[i]] = [1,i]



endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
