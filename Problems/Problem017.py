"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import time

startTime = time.clock()


def numLetters(n):
    x = {
        1:3,2:3,3:5,4:4,5:4,
        6:3,7:5,8:5,9:4,10:3,
        11:6,12:6,13:8,14:8,15:7,
        16:7,17:9,18:8,19:8,
        20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6
    }
    if (x.__contains__(n)):
        return x[n]

    if (n == 1000):
        return 3 + 8 #"one thousand"

    letters = 0

    if (n % 100 == 0):
        return (numLetters(int(n/100)) + 7)

    if (n >= 100 and n < 1000):
        hundreds = int(n / 100)
        letters += numLetters(hundreds) + 7 + 3 + numLetters(n - (hundreds * 100))

    if (n > 20 and n <= 99):
        tens = int(n / 10)
        letters += numLetters(tens*10)  + numLetters(n - tens*10)

    return letters

print(sum(numLetters(x) for x in range(1,1001)))

endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
