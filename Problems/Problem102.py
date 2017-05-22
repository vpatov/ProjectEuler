"""
 https://projecteuler.net/problem=102
 Triangle containment
Three distinct points are plotted at random on a Cartesian plane,
for which -1000 <= x , y <=1000, such that a triangle is formed.
Consider the following two triangles:
 A(-340,495), B(-153,-910), C(835,-947) 
X(-175,41), Y(-421,-714), Z(574,-645) 
 It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not. 
 Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing
 the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
 NOTE: The first two examples in the file represent the triangles in the example given above.
"""

import time
import operator
startTime = time.clock()


def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def vec_sub(v1,v2):
    return tuple([i - j for i,j, in zip(v1,v2)])


def dot(v1,v2):
    return sum([prod(i) for i in zip(v1,v2)])



##Algorithm taken from http://blackpawn.com/texts/pointinpoly/
##Very easy to implement
count = 0
f = open('input/input102.txt')
for line in f:
    nums = [int(i) for i in line.split(',')]
    verts = set([(nums[0],nums[1]),(nums[2],nums[3]),(nums[4],nums[5])])
    p1 = min(verts)
    verts.remove(p1)
    p2,p3 = verts.pop(),verts.pop()

    vec1 = vec_sub(p3,p1)
    vec2 = vec_sub(p2,p1)
    vec3 = vec_sub((0,0),p1)


    dot00 = dot(vec1, vec1)
    dot01 = dot(vec1, vec2)
    dot02 = dot(vec1, vec3)
    dot11 = dot(vec2, vec2)
    dot12 = dot(vec2, vec3)

    invDenom = 1.0 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    if (u >= 0)and (v >= 0) and (u + v < 1):
        count += 1




print count

endTime = time.clock()
print "Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds."
