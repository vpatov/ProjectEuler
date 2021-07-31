"""
 https://projecteuler.net/problem=142
 Perfect Square Collection

 Find the smallest x + y + z with integers x &gt; y &gt; z &gt; 0 such that x + y, x - y, x + z, x - z, y + z, y - z are all perfect squares.
"""
import time
import numpy as np
startTime = time.perf_counter()

#code
endTime = time.perf_counter()
print('Time elapsed:', '{:0.6f}'.format(endTime-startTime), 'seconds.')
