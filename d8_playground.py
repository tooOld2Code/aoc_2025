# Day 8: Playground
# /learn/aoc_2025/d8_playground.py
import math
from collections import defaultdict
import numpy as np

fl_pzl_input = '../aoc_2025/d8_jboxes.txt'
fl_tst_input = '../aoc_2025/d8_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
  mx_jb = 10
else:
  curr_fl = fl_pzl_input
  mx_jb = 1000

# modify as needed for current input
with open(curr_fl, "r") as f:
  d8_vals = [line.strip() for line in f]
d8_vals = [tuple(map(int, ln.split(","))) for ln in d8_vals]

distances = []
for i in range(len(d8_vals)):
  for j in range(i + 1, len(d8_vals)):
    dist = math.dist(d8_vals[i], d8_vals[j])
    distances.append((dist, (d8_vals[i], d8_vals[j])))
distances.sort(key=lambda x: x[0])


# part 1
def part_1():
  global distances
  rslt = 0
  dists = distances[:mx_jb]
  circs = {i: set() for i in range(mx_jb)}
  used_circs = -1
  circ_ndx_by_jbox = {}
  for _, (b1, b2) in distances:
    circ_ndx_by_jbox[b1] = -1
    circ_ndx_by_jbox[b2] = -1

  for _, (b1, b2) in dists:
    c1 = circ_ndx_by_jbox[b1]
    c2 = circ_ndx_by_jbox[b2]
    if c1 == -1 and c2 == -1:
        used_circs += 1
        circs[used_circs].update([b1, b2])
        circ_ndx_by_jbox[b1] = used_circs
        circ_ndx_by_jbox[b2] = used_circs
    elif c1 == -1:
        circs[c2].add(b1)
        circ_ndx_by_jbox[b1] = c2
    elif c2 == -1:
        circs[c1].add(b2)
        circ_ndx_by_jbox[b2] = c1
    elif c1 != c2:
      circs[c1].update(circs[c2])
      circ_ndx_by_jbox[b2] = circ_ndx_by_jbox[b1]
      for jb in circs[c2]:
        circ_ndx_by_jbox[jb] = c1
      circs[c2] = set()

  c_lens = [len(v) for k, v in circs.items()]
  c_lens.sort()
  rslt = math.prod(c_lens[-3:])
  return rslt


# part 2
def part_2():
  rslt = 0
  circs = defaultdict(set)
  used_circs = -1
  circ_ndx_by_jbox = {}
  for _, (b1, b2) in distances:
    circ_ndx_by_jbox[b1] = -1
    circ_ndx_by_jbox[b2] = -1
  n_circs = 0
  ok_stop = False

  for _, (b1, b2) in distances:
    c1 = circ_ndx_by_jbox[b1]
    c2 = circ_ndx_by_jbox[b2]
    if not ok_stop:
      ok_stop = (n_circs >= 5)
    if c1 == -1 and c2 == -1:
        used_circs += 1
        circs[used_circs].update([b1, b2])
        circ_ndx_by_jbox[b1] = used_circs
        circ_ndx_by_jbox[b2] = used_circs
        n_circs += 1
    elif c1 == -1:
        circs[c2].add(b1)
        circ_ndx_by_jbox[b1] = c2
    elif c2 == -1:
        circs[c1].add(b2)
        circ_ndx_by_jbox[b2] = c1
    elif c1 != c2:
      circs[c1].update(circs[c2])
      circ_ndx_by_jbox[b2] = circ_ndx_by_jbox[b1]
      for jb in circs[c2]:
        circ_ndx_by_jbox[jb] = c1
      del circs[c2]
      n_circs -= 1
    if n_circs == 1 and ok_stop:
      k = list(circs.keys())
      k = k[0]
      if len(circs[k]) == len(d8_vals):
        rslt = b1[0] * b2[0]
        break
  return rslt


print(f"Day 8, Part 1: {part_1()}")
print(f"Day 8, Part 2: {part_2()}")
