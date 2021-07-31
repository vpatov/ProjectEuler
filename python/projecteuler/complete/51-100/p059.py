"""
 https://projecteuler.net/problem=59
 XOR decryption

 Each character on a computer is assigned a unique code and the preferred standard is ASCII
 (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
 A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given
 value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the
 cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
 For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
 bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves",
 it is impossible to decrypt the message.

 Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the
 password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance
 for this method is using a sufficiently long password key for security, but short enough to be memorable.
 Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt
 (right click and \'Save Link/Target As...\'), a file containing the encrypted ASCII codes, and the knowledge that the
  plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

## password can be anything ranging from aaa,aab,...,zzy,zzz -> 26^3 possibilities

import time
from projecteuler.utils.getinput import getinput, getmisc
import string
startTime = time.perf_counter()

maxRatio = 0
answerKey = None

punctuation = set(string.punctuation)


f1 = getmisc('20k_words.txt')
words = set()
for line in f1:
    words.add(line.strip())

f2 = getinput(59)
partialInput = []
nums = None
for line in f2:
    line = line.strip()
    nums = line.split(',')
    #to make processing faster, only process the first 30 characters for starters.
    for num in nums[0:30]:
        partialInput.append(int(num))

def isEnglish(word):
    global words
    word = word.lower()
    word = ''.join(letter for letter in word if letter not in punctuation)

    return words.__contains__(word)

def process(key,ciphertext):
    keyPos = 0
    plaintext = []
    for char in ciphertext:
        plaintext.append(chr(ord(key[keyPos]) ^ char))
        keyPos = (keyPos + 1) % 3
    return ''.join(plaintext)

for i in range(ord('a'),ord('z') + 1):
    for j in range(ord('a'),ord('z') + 1):
        for k in range(ord('a'),ord('z') + 1):
            plaintext = process(chr(i) + chr(j) +chr(k),partialInput)
            plaintextWords = plaintext.split(' ')
            ratio = (sum(1 for word in plaintextWords if (isEnglish(word)))) / len(plaintextWords)
            if (ratio > maxRatio):
                maxRatio = ratio
                answerKey = (chr(i) + chr(j) + chr(k))



#once we've found the candidate password, now lets decrypt the entire message to get the sum of the ascii characters
fullInput = []
for num in nums:
    fullInput.append(int(num))

plaintext = process(answerKey,fullInput)
print(sum(ord(a) for a in plaintext))










endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
