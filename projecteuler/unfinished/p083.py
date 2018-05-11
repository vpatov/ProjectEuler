"""
 https://projecteuler.net/problem=83
 Path sum: four ways

 NOTE: This problem is a significantly more challenging version of Problem 81 . 
 In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297. 
 
$$
\\begin{pmatrix}
\\color{red}{131} &amp; 673 &amp; \\color{red}{234} &amp; \\color{red}{103} &amp; \\color{red}{18}\\\\
\\color{red}{201} &amp; \\color{red}{96} &amp; \\color{red}{342} &amp; 965 &amp; \\color{red}{150}\\\\
630 &amp; 803 &amp; 746 &amp; \\color{red}{422} &amp; \\color{red}{111}\\\\
537 &amp; 699 &amp; 497 &amp; \\color{red}{121} &amp; 956\\\\
805 &amp; 732 &amp; 524 &amp; \\color{red}{37} &amp; \\color{red}{331}
\\end{pmatrix}
$$
 
 Find the minimal path sum, in matrix.txt (right click and 
"Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
"""

import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
