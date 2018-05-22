"""
 https://projecteuler.net/problem=63
 Powerful digit counts


 The 5-digit number, 16807=7^5 , is also a fifth power. Similarly, the 9-digit number, 134217728=8^9 , is a ninth power. 
 How many n -digit positive integers exist which are also an n th power?
"""

import time
startTime = time.clock()


count = 0
p = 1
while(p < 1000):
  i = 1
  num = i**p
  while len(str(num)) <= p:
    if len(str(num)) == p:
      count+=1
    i += 1
    num = i**p

  p+=1

print(count)




endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
