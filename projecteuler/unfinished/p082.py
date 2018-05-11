"""
 https://projecteuler.net/problem=82
 Path sum: three ways

 NOTE: This problem is a more challenging version of Problem 81 . 
 The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994. 
 
$$
\\begin{pmatrix}
131 &amp; 673 &amp; \\color{red}{234} &amp; \\color{red}{103} &amp; \\color{red}{18}\\\\
\\color{red}{201} &amp; \\color{red}{96} &amp; \\color{red}{342} &amp; 965 &amp; 150\\\\
630 &amp; 803 &amp; 746 &amp; 422 &amp; 111\\\\
537 &amp; 699 &amp; 497 &amp; 121 &amp; 956\\\\
805 &amp; 732 &amp; 524 &amp; 37 &amp; 331
\\end{pmatrix}
$$
 
 Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
