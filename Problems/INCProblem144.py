import math
"""
 https://projecteuler.net/problem=144
 Investigating multiple reflections of a laser beam

 In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. The beam enters the cell,
 bounces around on the mirrors, and eventually works its way back out.
 The specific white cell we will be considering is an ellipse with the equation 4 x ^2 + y ^2 = 100 
 The section corresponding to -0.01 x 
 
 The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, and the beam first impacts
 the mirror at (1.4,-9.6).
 Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection "angle of incidence
 equals angle of reflection." That is, both the incident and reflected beams make the same angle with the normal line at
 the point of incidence.
 In the figure on the left, the red line shows the first two points of contact between the laser beam and the wall of the
 white cell; the blue line shows the line tangent to the ellipse at the point of incidence of the first bounce. The slope m of
 the tangent line at any point ( x , y ) of the given ellipse is: m = -4 x / y The normal line is perpendicular to this tangent
  line at the point of incidence.
 The animation on the right shows the first 10 reflections of the beam. 

 How many times does the beam hit the internal surface of the white cell before exiting?
"""

import time
startTime = time.clock()

class line:
    def __init__(self,m,b):
        self.m = m
        self.b = b

    def __repr__(self):
        return 'y = ' + str(self.m) + 'x + ' + str(self.b)

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return point(self.x + other.x,self.y + other.y)

    def __sub__(self, other):
        return point(self.x - other.x,self.y - other.y)

    def __repr__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)

def line_from_two_points(p1,p2):
    slope = float(p2.y - p1.y) / (p2.x - p1.x)
    intercept = p2.y - (slope * p2.x)
    return line(slope,intercept)

def perpendicular_line(line_,p):
    slope = -1.0 / line_.m
    intercept = p.y - (slope * p.x)
    return line(slope,intercept)

def reflect_line(base,refl,p):
    m1 = base.m
    m2 = refl.m
    slope = float(2*m1 + (m2 * m1 * m1) - m2) / float(2 * m1 * m2 - (m1 * m1) + 1)
    intercept = p.y - (slope * p.x)
    return line(slope,intercept)

def slope_tangent(p):
    return -4.0 * p.x / p.y

def tangent_line(p):
    slope = slope_tangent(p)
    intercept = p.y - (slope * p.x)
    return line(slope,intercept)

#quadratic formula
# -b +/- sqrt(b^2 - 4ac) / 2a
def get_roots(a,b,c):
    expr = math.sqrt(b*b - (4*a*c))
    return ((-b + expr) / (2*a),(-b - expr) / (2 * a))

def intersection_ellipse(line):
    m,b = line.m,line.b
    a,b,c = float(4 + (m*m)),float(-2*m*b),float((b*b) - 100)
    roots = get_roots(a,b,c)
    return (-roots[0],-roots[1])



count = 1
old_point = point(0,10.1)
new_point = point(1.4,-9.6)
while (True):
    line1 = line_from_two_points(old_point,new_point)
    tangent_line1 = tangent_line(new_point)
    perp_tangent_line1 = perpendicular_line(tangent_line1,new_point)
    new_line = reflect_line(perp_tangent_line1,line1,new_point)
    roots = intersection_ellipse(new_line)
    root1,root2 = roots
    new_x = root1

    if (math.fabs(root1 - new_point.x) <= 0.00001):
        new_x = root2

    new_y = (new_line.m * new_x) + new_line.b
    old_point = new_point
    new_point = point(new_x,new_y)
    if (new_x <= 0.01 and new_x >= -0.01 and new_y > 0):
        break
    count += 1


print count



endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
