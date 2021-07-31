"""
Find the number of integers 1 < n < 107, 
for which n and n + 1 have the same number of positive divisors. 

For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""
import time
import subprocess
startTime = time.perf_counter()


result = subprocess.run('gcc p179.c -o p179 -lm',shell=True)
if (result.returncode != 0):
    print("Make sure the c file is present. Are you in the right directory?")
else:
    print(subprocess.getoutput('./p179'))


#code
endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
