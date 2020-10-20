"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import time
from projecteuler.utils.getinput import getinput
startTime = time.perf_counter()

names = None


f = getinput(22)
for line in f:
    names = line.split(",")

names.sort()

def score(name):
    score = 0
    for letter in name:
        if (letter.isalpha()):
            score += ord(letter) - ord('A') + 1
    return score

totalScore = 0
for i in range(0,len(names)):
    totalScore += score(names[i]) * (i+1)

print(totalScore)

endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
