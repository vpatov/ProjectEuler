"""
 https://projecteuler.net/problem=75
 Singular integer right triangles

 It turns out that 12 cm is the smallest length of wire that can be bent to form an integer
 sided right angle triangle in exactly one way, but there are many more examples.
 12 cm : (3,4,5) 24 cm : (6,8,10) 30 cm : (5,12,13) 36 cm : (9,12,15) 40 cm : (8,15,17) 48 cm : (12,16,20) 
 In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
  and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to
  form exactly three different integer sided right angle triangles.
 120 cm : (30,40,50), (20,48,52), (24,45,51) 
 Given that L is the length of the wire, for how many values of L
"""

import time
startTime = time.perf_counter()

target = 1_500_000

triplets = set()
# m > n
upper_bound = 1000
for n in range(1,upper_bound):
  for m in range(n+1,upper_bound):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2

    triplet = (a,b,c)
    if sum(triplet) > target:
      break
    
    triplets.add(tuple(sorted(triplet)))

print("Calculated primitive triplets")

list_triplets = list(triplets)
for triplet in list_triplets:
  a,b,c = triplet
  cur = triplet
  while(True):
    if sum(cur) > target:
      break
    triplets.add(tuple(sorted(cur)))
    cur = (cur[0] + a, cur[1] + b, cur[2] + c)
 
print("Generated multiples of primitive triplets")


triplet_sums = dict()
for triplet in triplets:
  s = sum(triplet)
  if s in triplet_sums:
    triplet_sums[s].append(triplet)
  else:
    triplet_sums[s] = [triplet]

print("Created triplet_sums dict")

tot_sum = 0
for triplet_sum in triplet_sums:
  if len(triplet_sums[triplet_sum]) == 1:
    tot_sum += 1

print(tot_sum)
    




endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
