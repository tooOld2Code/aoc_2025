# Day 9: ???
# /learn/aoc_2025/d9_theater.py
import math
from collections import defaultdict

fl_pzl_input = '../aoc_2025/d9_tiles.txt'
fl_tst_input = '../aoc_2025/d9_tst.txt'

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


def get_area(p1, p2):
  return (abs(p1[0]-p2[0]) + 1) * (abs(p1[1]-p2[1]) + 1)


# part 1
def part_1():
  mx_area = 0
  l_cnt = -1
  # get area for top 1/8 of distances, 1/8 is a guess,
  # but it did work for my puzzle data
  for dst, (p1, p2) in distances[:len(distances)//8]:
    l_cnt += 1
    t_area = get_area(p1, p2)
    if t_area >= mx_area:
      mx_area = t_area
  return mx_area


# part 2
def part_2():
  # get all edges of valid tile area
  # for each possible rectangle, see if any edges are in it
  rslt = 0
  n_r = len(d9_vals)

  edges, areas = [], []
  for i in range(n_r):
    edges.append(sorted((d9_vals[i], d9_vals[i-1])))
    for j in range(i+1, n_r):
      r1, r2 = sorted((d9_vals[i], d9_vals[j]))
      areas.append((get_area(r1, r2), r1, r2)) 

  edges.sort(reverse=True, key=lambda e: get_area(e[0], e[1]))
  areas.sort(reverse=True)

  for sz, (x1, y1), (x2, y2) in areas:
    y1, y2 = sorted((y1, y2))
    # if any edge in rectangle, it is not valid
    if not any((x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
      for (x3, y3), (x4, y4) in edges):
      rslt = sz
      break
 
  return rslt


print(f"Day 9, Part 1: {part_1()}")
print(f"Day 9, Part 2: {part_2()}")
