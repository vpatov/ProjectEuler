"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import time
startTime = time.clock()

sum = 0
fibNums = [1,2]

index = 1
while (fibNums[index] < 4000000):
    fibNums.append(fibNums[index] + fibNums[index-1])
    if (fibNums[index] % 2 == 0):
        sum += fibNums[index]
    index += 1

print(sum)


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")



