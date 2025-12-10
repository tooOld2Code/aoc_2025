# Day 5: Cafeteria
# /learn/aoc_2025/d5_cafe.py
# import numpy as np

fl_pzl_input = '../aoc_2025/d5_food.txt'
fl_tst_input = '../aoc_2025/d5_tst.txt'

# Change to False when finished dev and testing to run on puzzle 
use_test = False
if use_test:
  curr_fl = fl_tst_input
else:
  curr_fl = fl_pzl_input

# modify as needed for current input
fresh = []
avail = []

with open(curr_fl, "r") as f:
  for line in f:
    if line == "\n":
      continue
    if "-" in line:
      st, nd = line.strip().split('-')
      fresh.append((int(st), int(nd)))
    else:
      avail.append(int(line.strip()))

fresh.sort()

# part 1
def part_1():
  rslt = 0
  for id in avail:
    for rng in fresh:
      if id >= rng[0] and id <= rng[1]:
        rslt += 1
        break
  return rslt


# part 2
def part_2():
  rslt = 0
  # merge ranges
  merged = []
  c_low, c_hi = fresh[0]
  for n_low, n_hi in fresh[1:]:
    if n_low <= c_hi + 1:
      c_hi = max(c_hi, n_hi)
    else:
      merged.append((c_low, c_hi))
      c_low, c_hi = n_low, n_hi
  merged.append((c_low, c_hi))
  rslt = sum(hi - lw + 1 for lw, hi in merged)
  return rslt


print(f"Day X, Part 1: {part_1()}")
print(f"Day X, Part 2: {part_2()}")
