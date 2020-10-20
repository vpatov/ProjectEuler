"""
 https://projecteuler.net/problem=145
 How many reversible numbers are there below one-billion?

 Some positive integers n have the property that the sum [ n + reverse( n ) ] consists entirely 
 of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers 
 reversible ; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or 
 reverse( n ). 

 There are 120 reversible numbers below one-thousand. 

 How many reversible numbers are there below one-billion (10^9 )?
"""
import time
import subprocess
startTime = time.perf_counter()


result = subprocess.run('gcc p145.c -pthread -o p145',shell=True)
if (result.returncode != 0):
    print("Make sure the c file is present. Are you in the right directory?")
else:
    print(subprocess.getoutput('./p145'))


#code
endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')

