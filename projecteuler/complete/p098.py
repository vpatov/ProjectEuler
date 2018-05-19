"""
 https://projecteuler.net/problem=98
 Anagramic squares

 By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2 . What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2 . We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter. 
 Using words.txt (right click and \'Save Link/Target As...\'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself). 
 What is the largest square number formed by any member of such a pair? 
 NOTE: All anagrams formed must be contained in the given text file.
"""
import time
import numpy as np
import math
import itertools
from projecteuler.utils.getinput import getinput
startTime = time.clock()


class mystr(str):
   def mycount(self,char):
      return (self.count(char),char)

words = [mystr(word[1:-1]) for word in getinput(98).read().split(",")]

word_anagrams = dict()
for word in words:
  base = ''.join(sorted(word,key=word.mycount))
  if base in word_anagrams:
    word_anagrams[base].append(word)
  else:
    word_anagrams[base] = [word]


word_anagrams = [tuple(anagrams) for anagrams in word_anagrams.values() if len(anagrams) > 1]
temp = []
for anagram in word_anagrams:
  if len(anagram) == 2:
    temp.append(anagram)
  else:
    for combo in itertools.combinations(anagram,2):
      temp.append(combo)

word_anagrams = temp

maxlen = max([max([len(word) for word in words]) for words in word_anagrams])
maxprod = 9**maxlen
limit = int(math.sqrt(maxprod))
squares = [num**2 for num in range(4,limit)]



numerical_anagrams = {numlength:{} for numlength in range(2,maxlen+1)}
numlength = 2
for square in squares:
  strnum = mystr(square)
  numlength = len(strnum)
  base = ''.join(sorted(strnum,key=strnum.mycount))
  if base in numerical_anagrams[numlength]:
    numerical_anagrams[numlength][base].append(square)
  else:
    numerical_anagrams[numlength][base] = [square]

numerical_anagrams = {
  numlength: {
    base:numerical_anagrams[numlength][base] for base in numerical_anagrams[numlength] if len(numerical_anagrams[numlength][base]) > 1
  }
  for numlength in numerical_anagrams
}



count_pairs = 0
max_square = 0
for anagram in word_anagrams:
  length = len(anagram[0])
  word1,word2 = anagram
  skip_word = False
  for numbase in numerical_anagrams[length]:
    if skip_word:
      break
    nums = numerical_anagrams[length][numbase]
    for num in nums:
      strnum = str(num)
      if len(set(strnum)) != len(set(word1)):
        continue
      digit_assignment = {char:None for char in word1}
     
      invalid = False 
      for char,digit in zip(word1,strnum):
        if digit_assignment[char] != None:
          invalid = True
          break
        digit_assignment[char] = digit
      if invalid:
        continue

      resnumber = ''
      for char in word2:
        resnumber += digit_assignment[char]

      resnumber = int(resnumber)
      if resnumber in nums:
        count_pairs += 1
        skip_word = True
        max_square = max(num,resnumber,max_square)
        break

print(max_square)

endTime = time.clock()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
