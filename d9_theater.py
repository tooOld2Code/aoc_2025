# Day 9: ???
# /learn/aoc_2025/d9_theater.py
import math
# import numpy as np
# import pandas as pd

fl_pzl_input = '../aoc_2025/d9_tiles.txt'
fl_tst_input = '../aoc_2025/d9_tst.txt'

# def inp_to_numpy(dD_in):
#   rdgs = [[int(bd) for bd in rdg.strip()] for rdg in dD_in]
#   r_np = np.array(rdgs)
#   return r_np

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
with open(curr_fl, "r") as f:
  d9_vals = [line.strip() for line in f]
d9_vals = [tuple(map(int, ln.split(","))) for ln in d9_vals]

distances = []
for i in range(len(d9_vals)):
  for j in range(i + 1, len(d9_vals)):
    dist = math.dist(d9_vals[i], d9_vals[j])
    distances.append((dist, (d9_vals[i], d9_vals[j])))
distances.sort(key=lambda x: x[0], reverse=True)

if use_test:
  print(distances)

# part 1
def part_1():
  rslt = 0
  mx_area = 0
  for _, (p1, p2) in distances[:len(distances)//4]:
    t_area = (abs(p1[0]-p2[0]) + 1) * (abs(p1[1]-p2[1]) + 1)
    if t_area >= mx_area:
      mx_area = t_area
    print(f"{(p1, p2)} -> {t_area} -> {mx_area}")
  
  return mx_area


# part 2
def part_2():
  rslt = 0
  return rslt


print(f"Day 9, Part 1: {part_1()}")
print(f"Day 9, Part 2: {part_2()}")
